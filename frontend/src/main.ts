/**
 * Top-level await requires ES2022 (at least) as target and module
 * for TypeScript compiler (check tsconfig.json)
 * https://caniuse.com/mdn-javascript_operators_await_top_level
 */

import { Notify, Quasar } from 'quasar';
import quasarLang from 'quasar/lang/es';
import { createApp } from 'vue';
import Root from '@/App.vue';
/* eslint-disable @typescript-eslint/no-restricted-imports */
import quasarIconSet from '@/plugins/quasar/material-icons';
import router from '@/plugins/router';
import createServerPlugin from '@/plugins/server/plugin';
/* eslint-enable @typescript-eslint/no-restricted-imports */

/**
 * - GLOBAL STYLES -
 */
import '@fontsource/jost';
import '@unocss/reset/normalize.css';
import '@unocss/reset/sanitize/assets.css';
import '@unocss/reset/sanitize/sanitize.css';
import 'quasar/dist/quasar.css';
import 'virtual:uno.css';

/* eslint-disable-next-line @typescript-eslint/no-unsafe-argument */
const app = createApp(Root);

app.use(router);
app.use(Quasar, {
  plugins: {
    Notify
  },
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
  lang: quasarLang,
  iconSet: quasarIconSet
});
app.use(createServerPlugin());

await router.isReady();
app.mount('#app');
