<template>
  <div class="flex justify-center items-center flex-col flex-content-center flex-wrap h-full">
    <h3>Iniciar sesión</h3>
    <p>Inicie sesión para acceder a las reservas y el historial de reservas de su gimnasio</p>
  </div>
  <div class="flex justify-center items-center flex-col flex-content-center flex-wrap">
    <QForm
      @submit="() => {
        $server.loginUser(username, password, rememberMe)
      }">
      <QInput
        v-model="username"
        class="form-field"
        filled
        label="Nombre de usuario"
        lazy-rules
        :rules="[
          val => val && val.length > 0 || emptyMessage,
          val => !val.includes(' ') || 'No puede tener espacios'
        ]" />

      <QInput
        v-model="password"
        class="form-field"
        filled
        label="Contraseña"
        lazy-rules
        :rules="[
          val => val && val.length > 0 || emptyMessage
        ]" />

      <div class="flex justify-center items-center flex-col flex-content-center flex-wrap">
        <QCheckbox
          v-model="rememberMe"
          label="Mantener la sesión iniciada" />
        <QSeparator />
        <QBtn
          label="Iniciar sesión"
          type="submit"
          color="primary" />
      </div>
    </QForm>
  </div>
</template>

<route lang="yaml">
  meta:
    title: "Iniciar sesión"
</route>

<script setup lang="ts">
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const rememberMe = ref(true);

const emptyMessage = 'Este campo no puede estar vacío';
</script>

<style scoped>
.form-field {
  width: 50vw;
}
</style>
