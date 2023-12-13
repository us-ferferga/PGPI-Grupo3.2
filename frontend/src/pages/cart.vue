<template>
  <h3 style="text-align: center">
    CARRITO
  </h3>
  <QList>
    <QItem
      v-for="item in cart.cart"
      :key="item.id">
      <QItemSection>
        <QImg
          v-if="getActivityFromProduct(item.id)?.image.data"
          :src="getActivityFromProduct(item.id)?.image.data" />
        <QItemLabel v-if="getActivityFromProduct(item.id)?.name">{{ getActivityFromProduct(item.id)?.name }}</QItemLabel>
      </QItemSection>
      <QItemSection side>
        <QItemLabel>{{ item.price }}€</QItemLabel>
      </QItemSection>
    </QItem>
  </QList>
</template>

<script setup lang="ts">
import { Activity } from '@/api';
import { activities } from '@/composables/use-activities';
import { useCart } from '@/composables/use-cart';

const cart = useCart();

function getActivityFromProduct(id: number | undefined): Activity | undefined {
  return activities.value.find(i => i.id === id);
}

function updateQuantity(productId: number, quantity: number) {
  cart.value.quantityMap.set(productId, quantity);
}
</script>
