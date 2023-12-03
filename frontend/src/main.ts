/**
 * Top-level await requires ES2022 (at least) as target and module
 * for TypeScript compiler (check tsconfig.json)
 * https://caniuse.com/mdn-javascript_operators_await_top_level
 */

import { createApp } from 'vue';
import { Quasar } from 'quasar';
import quasarLang from 'quasar/lang/es';
import { VueQueryPlugin } from '@tanstack/vue-query';
import Root from '@/App.vue';
/* eslint-disable @typescript-eslint/no-restricted-imports */
import router from '@/plugins/router';
/* eslint-enable @typescript-eslint/no-restricted-imports */

/**
 * - GLOBAL STYLES -
 */
import '@fontsource/jost';
import 'quasar/dist/quasar.css';
import 'virtual:uno.css';
import '@unocss/reset/normalize.css';
import '@unocss/reset/sanitize/sanitize.css';
import '@unocss/reset/sanitize/assets.css';

/* eslint-disable-next-line @typescript-eslint/no-unsafe-argument */
const app = createApp(Root);

app.use(router);
app.use(Quasar, {
  config: {
    brand: {
      primary: '#000000',
      secondary: '#0d8276',
      accent: '#9C27B0',
      dark: '#1d1d1d',
      positive: '#21BA45',
      negative: '#C10015',
      info: '#1a6473',
      warning: '#F2C037'
    }
  },
  lang: quasarLang
});
app.use(VueQueryPlugin);

await router.isReady();
app.mount('#app');
