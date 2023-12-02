<template>
  <div class="card">
    <div class="q-pa-md row items-start q-gutter-md">
      <q-card flat bordered class="my-card">
        <q-card-section>
          <div class="text-h2">Nombre de la actividad</div>
        </q-card-section>

        <q-separator inset />

        <q-card-section>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua.
        </q-card-section>

        <q-card-section>
          Clase impartida por: Perro sanche
        </q-card-section>

        <q-card-section>
          Sala: Nombre de sala
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script setup lang="ts">
  
</script>

<style>
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