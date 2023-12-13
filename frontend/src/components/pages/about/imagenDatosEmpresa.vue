<template>
  <div
    class="q-pa-md q-gutter-md"
    style="margin-top: 50px;">
    <div class="row justify-between">
      <QParallax
        :height="300"
        :src="src" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { activities } from '@/composables/use-activities';
import { computed } from 'vue';

const src = computed(() => {
  return activities.value[Math.floor(Math.random() * activities.value.length)].image?.data;
});
</script>
