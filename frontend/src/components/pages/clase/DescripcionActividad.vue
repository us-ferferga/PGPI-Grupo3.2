<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <QCard
      flat
      bordered
      class="my-card">
      <QCardSection>
        <div class="text-h2">
          {{ props.activity.name }}
        </div>
      </QCardSection>
      <QSeparator inset />
      <QCardSection>
        {{ props.activity.description }}
      </QCardSection>

      <QCardSection>
        <b>Clase impartida por</b>: {{ props.activity.teacher.name }}
      </QCardSection>

      <QCardSection>
        <b>Sala</b>: {{ props.activity.class_space.name }}
      </QCardSection>
    </QCard>
  </div>
</template>

<script setup lang="ts">
import { Activity } from '@/api';

const props = defineProps<{ activity: Activity }>();
</script>
