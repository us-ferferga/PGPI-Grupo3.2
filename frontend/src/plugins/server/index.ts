/**
 * The 'server' plugin includes the tools needed to interact with the server:
 */
import {
  ActivityApi,
  AuthApi,
  Configuration,
  ProductsApi,
  User
} from '@/api';
import { mergeExcludingUnknown } from '@/utils/data-manipulation';
import { useStorage } from '@vueuse/core';
import axios, { AxiosError } from 'axios';
import { Notify } from 'quasar';
import { watch } from 'vue';

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
    rememberMe: false
  };
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
    baseURL: '127.0.0.1:8000',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
  public readonly activity = new ActivityApi(this._apiConfiguration, '', this._axios);
  public readonly products = new ProductsApi(this._apiConfiguration, '', this._axios);
  private readonly _auth = new AuthApi(this._apiConfiguration, '', this._axios);

  public get user(): User | undefined {
    return this._state.value.user;
  }

  public async loginUser(username: string, password: string, rememberMe = true): Promise<void> {
    try {
      const { data } = await this._auth.authLoginCreate({ username, password });

      this._state.value.rememberMe = rememberMe;

      if (!data.token) {
        throw new Error();
      }
    } catch (e) {
      let message = 'Error desconocido';
      if (isAxiosError(e) && e.response?.status === 401) {
        message = 'Credenciales inválidas';
      }
  
      Notify.create({
        message,
        color: 'red'
      })
    }
  }

  public async logoutUser(): Promise<void> {
    try {
      await this._auth.authLogoutCreate();
    } catch {} finally {
      this._state.value.token = undefined;
      this._state.value.user = undefined;
    }

  }

  public constructor() {
    /**
     * Configure app's axios instance to perform requests to the server and clear itself when necessary.
     */
    watch(() => this._state.value.token, () => {
      if (this._state.value.token) {
        this._axios.defaults.headers['Authorization'] = `Token ${this._state.value.token}`;
      } else {
        delete this._axios.defaults.headers['Authorization'];
      }
    });
  }
}

export const serverInstance = new ServerPlugin();


