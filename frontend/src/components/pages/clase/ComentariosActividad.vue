<template>
  <QForm class="pa-10">
    <QInput
      v-model="commentBody"
      filled
      type="textarea"
      label="Deja un comentario" />
    <div class="flex justify-end">
      <QBtn
        label="Enviar"
        type="submit"
        color="primary" />
    </div>
  </QForm>

  <QCard
    class="pa-10"
    flat
    bordered>
    <QCardSection horizontal>
      <div>
        <div
          v-for="comment in props.comments"
          :key="comment.id">
          <QChatMessage
            class="flex justify-end"
            size="12"
            :name="comment.user.username"
            :text="[comment.content]"
            sent />
        </div>
      </div>
    </QCardSection>
  </QCard>
</template>

<script setup lang="ts">
import { Comment } from '@/api';
import { ref } from 'vue';

const props = defineProps<{ comments: Comment[] }>();
const commentBody = ref('');
</script>
