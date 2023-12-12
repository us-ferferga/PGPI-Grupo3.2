<template>
  <div class="card">
    <div class="q-pa-md row items-start q-gutter-md">
      <QCard
        flat
        bordered
        class="my-card">
        <QCardSection>
          <div class="text-h2">
            {{ name }}
          </div>
        </QCardSection>

        <QSeparator inset />

        <QCardSection>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua.
        </QCardSection>

        <QCardSection>
          Clase impartida por: {{ teacher }}
        </QCardSection>

        <QCardSection>
          Sala: {{ sala }}
        </QCardSection>
      </QCard>
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
const name = activity.activity.name;
const teacher = activity.activity.teacher.name;
const sala = activity.class_space.name;

</script>

<style scoped>
  .card{
    height: 300px;
    width: 700px;
    opacity: 0; /* La imagen estará inicialmente invisible */
    animation: entradaDesdeIzquierda 1s ease-out forwards; /* Aplica la animación */
  }

  @keyframes entradaDesdeIzquierda {
    from {
      opacity: 0;
      transform: translateX(-100%); /* Desplaza la imagen hacia la izquierda al 100% de su ancho */
    }
    to {
      opacity: 1;
      transform: translateX(0); /* Sin desplazamiento, posición final en la izquierda */
    }
  }

</style>
