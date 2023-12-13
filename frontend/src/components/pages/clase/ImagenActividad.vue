<template>
  <div class="q-pa-md q-gutter-sm">
    <div>
      <QImg
        :src="props.activity.image.data"
        :ratio="16/9" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { Activity } from '@/api';

const props = defineProps<{ activity: Activity }>();
</script>
