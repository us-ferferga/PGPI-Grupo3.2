<template>
  <div class="flex justify-center items-center flex-col flex-content-center flex-wrap h-full">
    <h3>Iniciar sesión</h3>
    <p>Inicie sesión para acceder a las reservas y el historial de reservas de su gimnasio</p>
  </div>
  <div class="flex justify-center items-center flex-col flex-content-center flex-wrap">
    <QForm
      @submit="submitForm">
      <QInput
        v-model="username"
        class="form-field"
        filled
        label="Nombre de usuario"
        lazy-rules
        :disable="loading"
        :rules="[
          val => val && val.length > 0 || emptyMessage,
          val => !val.includes(' ') || 'No puede tener espacios'
        ]" />

      <QInput
        v-model="password"
        class="form-field"
        filled
        type="password"
        label="Contraseña"
        lazy-rules
        :disable="loading"
        :rules="[
          val => val && val.length > 0 || emptyMessage
        ]" />

      <div class="flex justify-center items-center flex-col flex-content-center flex-wrap">
        <QCheckbox
          v-model="rememberMe"
          :disable="loading"
          label="Mantener la sesión iniciada" />
        <QSeparator />
        <QBtn
          label="Iniciar sesión"
          :loading="loading"
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
import { useServer } from '@/composables';
import { ref } from 'vue';
import { useRouter } from 'vue-router/auto';

const server = useServer();
const router = useRouter();

const username = ref('');
const password = ref('');
const rememberMe = ref(true);
const loading = ref(false);

const emptyMessage = 'Este campo no puede estar vacío';

/**
 * Procesa los datos del formulario
 */
async function submitForm(): Promise<void> {
  try {
    loading.value = true;

    await server.loginUser(username.value, password.value, rememberMe.value);

    if (server.user) {
      await router.replace('/');
    }
  } catch {} finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.form-field {
  width: 50vw;
}
</style>
