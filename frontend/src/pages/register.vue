<template>
  <div class="flex justify-center items-center flex-col flex-content-center flex-wrap h-full">
    <h3>Registrarse</h3>
    <p>Regístrese para poder realizar reservas, publicar comentarios y gestionar sus incidencias de una forma más personalizada</p>
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
        v-model="email"
        class="form-field"
        filled
        label="Dirección de correo electrónico"
        lazy-rules
        :disable="loading"
        :rules="[
          val => val && val.length > 0 || emptyMessage,
          val => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) || 'Debe ser una dirección de correo electrónico válida'
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

      <QInput
        v-model="repeatPassword"
        class="form-field"
        filled
        type="password"
        label="Repetir contraseña"
        lazy-rules
        :disable="loading"
        :rules="[
          val => val && val.length > 0 || emptyMessage,
          val => val === password || 'Las contraseñas no coinciden'
        ]" />

      <div class="flex justify-center items-center flex-col flex-content-center flex-wrap">
        <QCheckbox
          v-model="rememberMe"
          :disable="loading"
          label="Mantener la sesión iniciada" />
        <QSeparator />
        <QBtn
          label="Registrarse"
          type="submit"
          :loading="loading"
          color="primary" />
      </div>
    </QForm>
  </div>
</template>

<route lang="yaml">
  meta:
    title: "Registrarse"
</route>

<script setup lang="ts">
import { useServer } from '@/composables';
import { ref } from 'vue';
import { useRouter } from 'vue-router/auto';

const server = useServer();
const router = useRouter();

const username = ref('');
const email = ref('');
const password = ref('');
const repeatPassword = ref('');
const rememberMe = ref(true);
const loading = ref(false);

const emptyMessage = 'Este campo no puede estar vacío';

/**
 * Procesa los datos del formulario
 */
async function submitForm(): Promise<void> {
  try {
    loading.value = true;

    await server.signUpUser(username.value, password.value, email.value, rememberMe.value);

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
