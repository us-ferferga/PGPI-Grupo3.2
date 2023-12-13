<template>
  <QLayout>
    <QHeader elevated>
      <QToolbar>
        <RouterLink
          v-slot="{ navigate }"
          to="/"
          custom>
          <QToolbarTitle
            class="cursor-pointer"
            @click="navigate">
            <QAvatar>
              <img src="/logo.png" />
            </QAvatar>
            TrainerBook
          </QToolbarTitle>
        </RouterLink>
        <CarritoHeader v-if="$server.user" />
        <UserAvatar v-if="$server.user" />
        <template v-else>
          <RouterLink
            v-slot="{ navigate }"
            to="/register"
            custom>
            <QBtn
              color="secondary"
              :disable="route.name === '/register'"
              text-color="white"
              label="Registrarse"
              class="mr-2"
              @click="navigate()" />
          </RouterLink>
          <RouterLink
            v-slot="{ navigate }"
            to="/login"
            custom>
            <QBtn
              color="white"
              :disable="route.name === '/login'"
              text-color="black"
              label="Iniciar sesión"
              @click="navigate()" />
          </RouterLink>
        </template>
      </QToolbar>
    </QHeader>

    <QPageContainer>
      <PageView />
    </QPageContainer>
  </QLayout>
</template>

<script setup lang="ts">
import { useActivities } from '@/composables';
import { useRoute } from 'vue-router/auto';

await useActivities();

const route = useRoute();
</script>
