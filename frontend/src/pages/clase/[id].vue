<template>
  <div
    v-if="activity"
    style="margin-top: 5%;">
    <div class="row">
      <div class="col-6">
        <DescripcionActividad :activity="activity" />
      </div>
      <div class="col-6">
        <ImagenActividad :activity="activity" />
      </div>
    </div>

    <div class="contenedor">
      <h2 style="display: flex;align-items: center;  justify-content: center;">
        Horario
      </h2>
      <TablaActividad :products="[]" />
    </div>
    <div class="row">
      <ComprarYa />
      <Carrito />
    </div>
    <QSeparator />
    <h3 style="margin-left: 20px;">
      Comentarios
    </h3>
    <ComentariosActividad :comments="comments" />
  </div>
  <h1 v-else>
    No se ha encontrado la actividad
  </h1>
</template>

<script setup lang="ts">
import { Comment, Product } from '@/api';
import { useServer } from '@/composables';
import { activities } from '@/composables/use-activities';
import { computed, ref, watch } from 'vue';
import { useRoute } from 'vue-router/auto';

const { params } = useRoute();
const server = useServer();
const comments = ref<Comment[]>([]);
const products = ref<Product[]>([]);
const id = computed(() => 'id' in params ? params.id : undefined);
const activity = computed(() => activities.value.find(i => i.id === Number(id.value)));

/**
 * Obtiene los comentarios de la actividad
 */
async function fetchData(): Promise<void> {
  if (id.value && activity.value) {
    const commentsResponse = await server.api.comment.commentList(Number(id.value));
    // Const productsResponse = await server.api.activity.activityProductsList(Number(id.value));

    comments.value = commentsResponse.data;
    // Products.value = productsResponse.data;
  }
}

await fetchData();

watch(id, fetchData);
</script>
