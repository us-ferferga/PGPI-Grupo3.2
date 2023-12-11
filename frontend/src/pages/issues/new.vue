<template>
  <h3>CREA UNA INCIDENCIA</h3>
  <QForm
    class="q-gutter-md">
    <QInput
      v-model="text"
      filled
      label="Título"
      dense />

    <QInput
      v-model="text"
      filled
      type="textarea"
      label="Escribe tu incidencia" />

    <div>
      <QBtn
        label="Submit"
        type="submit"
        color="primary" />
    </div>
  </QForm>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const text = ref('');

</script>
