import { App } from 'vue';
import { serverInstance } from '.';

/**
 * Installs the remote plugin into the Vue instance to enable the usage of
 * $remote to access all the tools for handling a connection to the Django backend.
 */
export default function createRemote(): {
  install: (app: App) => void;
} {
  return {
    install: (app: App): void => {
      /**
       * `server` is readonly but this is the one place it should actually be set
       */
      // eslint-disable-next-line @typescript-eslint/no-unnecessary-type-assertion, @typescript-eslint/no-unsafe-assignment
      (app.config.globalProperties.$server as typeof serverInstance) =
        serverInstance;
    }
  };
}
