<template>
  <h3 style="text-align: center">
    ACTIVIDADES
  </h3>
  <div
    class="q-pa-md"
    style="margin: 2%;">
    <div class="q-col-gutter-md row items-start">
      <div
        v-for="i in activities"
        :key="i.id"
        class="col-4">
        <RouterLink
          v-slot="{ navigate }"
          :to="`/clase/${i.id}`"
          custom>
          <QImg
            v-if="i.image"
            src="https://cdn.quasar.dev/img/parallax2.jpg"
            class="imagen animacion cursor-pointer"
            @click="navigate">
            <div class="absolute-full text-subtitle2 flex flex-center">
              <h4>{{ i.name }}</h4>
            </div>
          </QImg>
          <div
            v-else
            class="absolute-full text-subtitle2 flex flex-center">
            <h4>{{ i.name }}</h4>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { activities } from '@/composables/use-activities';

console.log(activities.value);
</script>

<style scoped>
  .imagen {
  opacity: 0; /* La imagen estará inicialmente invisible */
}

/* Definición de la animación */
@keyframes entradaDesdeAbajo {
  from {
    opacity: 0;
    transform: translateY(100%); /* Desplaza la imagen hacia abajo al 100% de su altura */
  }
  to {
    opacity: 1;
    transform: translateY(0); /* Sin desplazamiento, posición final en la parte superior */
  }
}

/* Aplicar la animación cuando se carga la página */
.animacion {
  animation: entradaDesdeAbajo 1s ease-out forwards;
}
</style>
