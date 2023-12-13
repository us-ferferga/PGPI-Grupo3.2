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
    <div
      v-if="$server.user"
      class="flex justify-end">
      <QBtn
        class="ma-3"
        :label="selected.length > 0 ? `Añadir al carrito (${selected.length} elementos)` : 'Añadir al carrito'"
        color="purple"
        @click="cart.concat(selected)">
        <IMdiCart />
      </QBtn>
      <RouterLink
        v-slot="{ navigate }"
        to="/cart"
        custom>
        <QBtn
          class="ma-3"
          color="white"
          text-color="black"
          :label="selected.length > 0 ? `Comprar ya (${selected.length} elementos)` : 'Comprar ya'"
          @click="() => {
            cart.concat(selected)
            navigate()
          }" />
      </RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Product } from '@/api';
import { useCart } from '@/composables/use-cart';
import { computed, ref } from 'vue';

const props = defineProps<{ products: Product[] }>();

const selected = ref([]);
const cart = useCart();

interface Column {
  name: string;
  align: 'center' | 'left' | 'right';
  label: string;
  field: string;
  sortable: boolean;
}

const columns: Array<Column> = [
  { name: 'dia_start', align: 'center', label: 'Día inicio', field: 'dia_start', sortable: true },
  { name: 'dia_fin', align: 'center', label: 'Día fin', field: 'dia_fin', sortable: true },
  { name: 'hora_start', align: 'center', label: 'Hora de inicio', field: 'hora_start', sortable: true },
  { name: 'hora_fin', align: 'center', label: 'Hora de fin', field: 'hora_fin', sortable: true },
  { name: 'aforo', align: 'center', label: 'Aforo', field: 'aforo', sortable: true }
];

const rows = computed(() => {
  return props.products.map((product) => {
    const fechaFin = product.product_hour_fin ? new Date(Date.parse(product.product_hour_fin)) : undefined;
    const fechaInicio = product.product_hour_init ? new Date(Date.parse(product.product_hour_init)) : undefined;
    const diaFin = fechaFin ? fechaFin.getDay() : undefined;
    const mesFin = fechaFin ? fechaFin.getMonth() : undefined;
    const yearFin = fechaFin ? fechaFin.getFullYear() : undefined;
    const stringFin = `${diaFin}/${mesFin}/${yearFin}`;
    const diaInicio = fechaInicio ? fechaInicio.getDay() : undefined;
    const mesInicio = fechaInicio ? fechaInicio.getMonth() : undefined;
    const yearInicio = fechaInicio ? fechaInicio.getFullYear() : undefined;
    const stringInicio = `${diaInicio}/${mesInicio}/${yearInicio}`;
    const horaInicio = fechaInicio ? fechaInicio.getHours() : undefined;
    const minutosInicio = fechaInicio ? fechaInicio.getMinutes() : undefined;
    const stringHoraInicio = `${horaInicio}:${minutosInicio}`;
    const horaFin = fechaFin ? fechaFin.getHours() : undefined;
    const minutosFin = fechaFin ? fechaFin.getMinutes() : undefined;
    const stringHoraFin = `${horaFin}:${minutosFin}`;

    return {
      'dia_start': stringInicio,
      'dia_fin': stringFin,
      'hora_start': stringHoraInicio,
      'hora_fin': stringHoraFin,
      'aforo': product.quantity
    };
  });
});

</script>
