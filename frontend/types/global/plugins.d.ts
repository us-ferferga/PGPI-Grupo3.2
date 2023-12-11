import type { serverInstance } from '@/plugins/server';

interface RouteTransition {
  enter: string;
  leave?: string;
}

declare module 'vue' {
  interface ComponentCustomProperties {
    readonly $server: typeof serverInstance;
  }
}

declare module 'vue-router' {
  interface RouteMeta {
    layout: 'default';
    title?: string | null;
    transition?: RouteTransition;
  }
}

/**
 * This is important: https://stackoverflow.com/a/64189046
 * https://www.typescriptlang.org/docs/handbook/modules.html
 */

export { };

