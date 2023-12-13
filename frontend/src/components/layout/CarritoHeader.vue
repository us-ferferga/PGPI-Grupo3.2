<template>
  <RouterLink
    v-slot="{ navigate }"
    to="/cart"
    custom>
    <QAvatar
      color="green"
      class="mr-2 cursor-pointer"
      @click="navigate">
      <IMdiCart />
      <QBadge
        v-if="cart.length > 0"
        color="red"
        floating>
        {{ cart.length }}
      </QBadge>
    </QAvatar>
  </RouterLink>
</template>

<script setup lang="ts">
import { useCart } from '@/composables/use-cart';

const cart = useCart();
</script>
