import { computed } from 'vue';
import {
  createRouter,
  createWebHashHistory
} from 'vue-router/auto';
import { useTitle } from '@vueuse/core';
import metaGuard from './middlewares/meta';

const router = createRouter({
  history: createWebHashHistory()
});

/**
 * Middlewares
 */
router.beforeEach(metaGuard);

/**
 * Handle page title changes
 */
const appTitle = 'TrainerBook';
const pageTitle = computed(() => {
  const title = router.currentRoute.value.meta.title?.trim();

  return title ? `${title} | ${appTitle}` : appTitle;
});

useTitle(pageTitle);

export default router;
