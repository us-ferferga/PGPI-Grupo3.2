/**
 * Top-level await requires ES2022 (at least) as target and module
 * for TypeScript compiler (check tsconfig.json)
 * https://caniuse.com/mdn-javascript_operators_await_top_level
 */

import { createApp } from 'vue';
import Root from '@/App.vue';
/* eslint-disable @typescript-eslint/no-restricted-imports */
import router from '@/plugins/router';

/**
 * - GLOBAL STYLES -
 */
import 'virtual:uno.css';
import '@unocss/reset/normalize.css';
import '@unocss/reset/sanitize/sanitize.css';
import '@unocss/reset/sanitize/assets.css';

/* eslint-disable-next-line @typescript-eslint/no-unsafe-argument */
const app = createApp(Root);

app.use(router);

await router.isReady();
app.mount('#app');
