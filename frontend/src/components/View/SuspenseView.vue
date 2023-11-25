<template>
  <Suspense
    v-bind="props">
    <slot />
  </Suspense>
</template>

<script setup lang="ts">
const props = defineProps<{
  suspensible?: boolean;
}>();
</script>
