<template>
  <div class="q-pa-md q-gutter-sm">
    <div>
      <QImg
        :src="imagen"
        :ratio="16/9"
        class="imagen" />
    </div>
  </div>
</template>

<script setup lang="ts">
import {useRoute} from 'vue-router/auto';
import { useServer } from '@/composables';

const server = useServer();
const route = useRoute();

const activityID = route.params?.id;

const activityResponse = await server.api.activity.activityProductsList(activityID);

const activity = activityResponse.data[0];
const imagen = activity.activity.image;

</script>

<style scoped>
  .imagen {
    height: 300px;
    width: 500px;
    opacity: 0; /* La imagen estará inicialmente invisible */
    animation: entradaDesdeDerecha 1s ease-out forwards;
  }

  @keyframes entradaDesdeDerecha {
    from {
      opacity: 0;
      transform: translateX(100%);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }
</style>
