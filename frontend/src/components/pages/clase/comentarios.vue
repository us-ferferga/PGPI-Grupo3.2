<template>
  <QCard
    class="my-card"
    flat
    bordered
    style="width: 800px; margin-right: 50px;">
    <QCardSection horizontal>
      <div class="q-pa-md comentario">
        <div
          v-for="i in 4"
          :key="i.id"
          style="width: 100%; max-width: 600px">
          <QChatMessage
            size="12"
            name="Carlos"
            :text="['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.']"
            sent />
        </div>
      </div>
    </QCardSection>
  </QCard>

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
</template>

<script setup lang="ts">
import { useServer } from '@/composables';
import {useRoute} from 'vue-router/auto';

const server = useServer();
const route = useRoute();

const activityId = route.params?.id;
const comentariosResponse = await server.api.comment.commentList(activityId);
const comentarios = comentariosResponse.data[0];

const contenido = comentarios.content;
const userName = comentarios.user.username;

console.log(contenido);
console.log(userName);


</script>

<style scoped>
  .comentario{
    margin-left: auto;
  }
</style>
