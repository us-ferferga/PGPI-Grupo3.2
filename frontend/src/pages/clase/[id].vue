<template>
  <div style="margin-top: 5%;">
    <div class="row">
      <div class="col-6">
        <Descripcion />
      </div>
      <div class="col-6">
        <Imagen />
      </div>
      <div class="row">
        <ComprarYa style="margin-left: 50px;" />
        <Carrito />
        <QForm
          class="q-gutter-md">
          <QInput
            v-model="text"
            filled
            type="textarea"
            label="Deja un comentario"
            style="width: 300px;" />
          <div>
            <QBtn
              label="Submit"
              type="submit"
              color="primary" />
          </div>
        </QForm>
      </div>
    </div>
    <Horario />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {useRoute} from 'vue-router/auto';

const route = useRoute();
console.log(route.params.id);


const text = ref('');
</script>
