/**
 * The 'server' plugin includes the tools needed to interact with the server:
 */
import {
  ActivityApi,
  AuthApi,
  CommentApi,
  Configuration,
  ProductsApi,
  User
} from '@/api';
import { mergeExcludingUnknown } from '@/utils/data-manipulation';
import { useStorage } from '@vueuse/core';
import axios, { AxiosError } from 'axios';
import { Notify } from 'quasar';
import { watchEffect } from 'vue';

interface AuthState {
  token?: string;
  user?: User;
  rememberMe: boolean;
}

/**
 * TypeScript type guard for AxiosError
 */
function isAxiosError(object: unknown): object is AxiosError {
  return !!(object && typeof object === 'object' && 'isAxiosError' in object);
}

class ServerPlugin {
  private _defaultState: AuthState = {
    token: undefined,
    user: undefined,
    rememberMe: false };
  private _state = useStorage(
    'auth',
    structuredClone(this._defaultState),
    localStorage,
    {
      mergeDefaults: (storageValue, defaults) =>
        mergeExcludingUnknown(storageValue, defaults)
    }
  );
  private readonly _apiConfiguration = new Configuration();
  private _axios = axios.create({
    /**
     * CAMBIAR SI ES NECESARIO
     */
    baseURL: import.meta.env.MODE === 'development' ? 'http://192.168.0.24:8000' : undefined,
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': '*'
    }
  });
  public readonly api = {
    activity: new ActivityApi(this._apiConfiguration, '', this._axios),
    products: new ProductsApi(this._apiConfiguration, '', this._axios),
    comment: new CommentApi(this._apiConfiguration, '', this._axios)
  };
  private readonly _auth = new AuthApi(this._apiConfiguration, '', this._axios);

  public get user(): User | undefined {
    return this._state.value.user;
  }

  private _dispatchError = (message = 'Error desconocido'): void => {
    Notify.create({
      message,
      color: 'red'
    });
  };

  public loginUser = async (username: string, password: string, rememberMe = true): Promise<void> => {
    try {
      const { data } = await this._auth.authLoginCreate({ username, password });

      this._state.value.rememberMe = rememberMe;

      if (!data.token) {
        // eslint-disable-next-line unicorn/error-message
        throw new Error();
      }

      this._state.value.token = data.token;

      const meResponse = await this._auth.authMeRetrieve();

      this._state.value.user = meResponse.data;
    } catch (error) {
      this._dispatchError(isAxiosError(error) && error.response?.status === 401 ? 'Credenciales inválidas' : undefined);
    }
  };

  public logoutUser = async (): Promise<void> => {
    try {
      await this._auth.authLogoutCreate();
    } catch {} finally {
      this._clearState();
    }
  };

  public signUpUser = async (username: string, password: string, email: string, rememberMe = true): Promise<void> => {
    try {
      await this._auth.authRegisterCreate({ username, password, email });
      await this.loginUser(username, password, rememberMe);
    } catch (error) {
      this._dispatchError(isAxiosError(error) && error.response?.status === 409 ? 'El usuario ya existe' : undefined);
    }
  };

  private _clearState = (): void => {
    delete this._axios.defaults.headers.common.Authorization;
    this._state.value.token = undefined;
    this._state.value.user = undefined;
  };

  public constructor() {
    if (!this._state.value.rememberMe) {
      this._clearState();
    }

    /**
     * Configure app's axios instance to perform requests to the server and clear itself when necessary.
     */
    watchEffect(async () => {
      if (this._state.value.token) {
        try {
          this._axios.defaults.headers.common.Authorization = `Token ${this._state.value.token}`;

          const { data } = await this._auth.authMeRetrieve();

          this._state.value.user = data;
        } catch {
          this._dispatchError();
          this._clearState();
        }
      } else {
        this._clearState();
      }
    });
  }
}

export const serverInstance = new ServerPlugin();


