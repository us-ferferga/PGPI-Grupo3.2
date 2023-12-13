<template>
  <QForm
    v-if="$server.user"
    class="pa-10">
    <QInput
      v-model="commentBody"
      filled
      type="textarea"
      label="Deja un comentario" />
    <div class="flex justify-end">
      <QBtn
        :loading="loading"
        label="Enviar"
        type="submit"
        color="primary"
        @click.prevent="submitComment" />
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
import { useServer } from '@/composables';
import { ref } from 'vue';

const props = defineProps<{ comments: Comment[], id: number }>();
const emit = defineEmits<{
  'update': [];
}>();
const server = useServer();
const commentBody = ref('');
const loading = ref(false);

/**
 * Send comment
 */
async function submitComment(): Promise<void> {
  try {
    loading.value = true;
    await server.api.comment.commentCreateCreate({
      activity: props.id,
      content: commentBody.value
    });
    emit('update');
  } catch {} finally {
    loading.value = false;
  }
}
</script>
