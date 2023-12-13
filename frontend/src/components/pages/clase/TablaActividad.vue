<template>
  <div class="q-pa-md">
    <QTable
      v-model:selected="selected"
      style="height: 400px"
      flat
      bordered
      :rows="rows"
      :columns="columns"
      row-key="name"
      hide-bottom
      virtual-scroll
      selection="multiple" />
    <div class="flex justify-end">
      <QBtn
        square
        :label="selected.length > 0 ? `Añadir al carrito(${selected.length})` : 'Añadir al carrito'"
        color="purple">
        <IMdiCart />
      </QBtn>
      <QBtn
        color="white"
        text-color="black"
        :label="selected.length > 0 ? `Comprar ya (${selected.length} elementos)` : 'Comprar ya'" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { Product } from '@/api';
import { computed, ref } from 'vue';

const props = defineProps<{ products: Product[] }>();

const selected = ref([]);

interface Column {
  name: string;
  align: 'center' | 'left' | 'right';
  label: string;
  field: string;
  sortable: boolean;
}

const columns: Array<Column> = [
  { name: 'dia', align: 'center', label: 'Día', field: 'dia', sortable: true },
  { name: 'hora_start', align: 'center', label: 'Hora de inicio', field: 'hora_start', sortable: true },
  { name: 'hora_start', align: 'center', label: 'Hora de inicio', field: 'hora_start', sortable: true }
];

const rows2 = computed(() => {
  return props.products.map((product) => {
    return {
      dia: new Date(product.product_hour_fin)
    };
  });
});

const rows = [
  {
    dia: 'Lunes',
    hora: '10:30'
  },
  {
    dia: 'Martes',
    hora: '10:30'
  },
  {
    dia: 'Martes',
    hora: '18:30'
  },
  {
    dia: 'Jueves',
    hora: '10:30'
  },
  {
    dia: 'Viernes',
    hora: '10:30'
  }
];
</script>
