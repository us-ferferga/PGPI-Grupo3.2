<template>
  <div style="margin-top: 5%;">
    <div class="row">
      <div class="col-6">
        <Descripcion />
      </div>
      <div class="col-6">
        <Imagen />
      </div>
    </div>
    <Horario />
    <div class="row">
      <ComprarYa />
      <Carrito />
    </div>
    <q-separator />
    <h3 style="margin-left: 20px;">Comentarios</h3>
    <div class="row">
      <Comentarios></Comentarios>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';


const text = ref('');
</script>
