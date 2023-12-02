<template>
  <div class="q-pa-md q-gutter-sm">
    <div>
        <q-img
          src="https://picsum.photos/500/300"
          :ratio="16/9"
          img-class="imagen"
        />
      </div>
  </div>
</template>

<script setup lang="ts">
  
</script>

<style>
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