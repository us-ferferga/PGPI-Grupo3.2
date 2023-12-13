<template>
  <RouterLink
    v-slot="{ navigate }"
    to="/cart"
    custom>
    <QBtn :disable="cart.cart.length === 0" @click="() => navigate">
      <IMdiCart />
      <QBadge
        v-if="cart.cart.length > 0"
        color="red"
        floating>
        {{ cart.cart.length }}
      </QBadge>
    </QBtn>
  </RouterLink>
</template>

<script setup lang="ts">
import { useCart } from '@/composables/use-cart';

const cart = useCart();
</script>
