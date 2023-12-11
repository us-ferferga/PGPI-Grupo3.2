/* eslint-disable-next-line @typescript-eslint/no-restricted-imports */
import { serverInstance } from '@/plugins/server';

/**
 * Returns the server plugin instance. Equivalent to using `$server` inside
 * templates.
 *
 * Also needed when used outside setup functions or anywhere else
 * outside the Vue app instance.
 */
export function useServer(): typeof serverInstance {
  return serverInstance;
}
