<template>
  <QAvatar
    color="blue"
    class="cursor-pointer">
    <IFluentPerson28Filled />
    <QMenu
      transition-show="jump-down"
      transition-hide="jump-up">
      <QList style="min-width: 100px">
        <RouterLink
          v-slot="{ navigate }"
          to="/orders"
          custom>
          <QItem
            clickable
            @click="navigate()">
            <QItemSection>Mis pedidos</QItemSection>
          </QItem>
        </RouterLink>
        <QSeparator />
        <QItem clickable>
          <QItemSection>Cerrar sesión</QItemSection>
        </QItem>
      </QList>
    </QMenu>
  </QAvatar>
</template>

<script setup lang="ts">
</script>
