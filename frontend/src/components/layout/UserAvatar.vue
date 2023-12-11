<template>
  <QAvatar
    color="blue"
    class="cursor-pointer">
    <IFluentPerson28Filled />
    <QMenu
      transition-show="jump-down"
      transition-hide="jump-up">
      <div class="row no-wrap q-pa-md pb-0">
        <div class="row items-center">
          <QAvatar size="50px">
            <IFluentPerson28Filled />
          </QAvatar>
          <div
            v-if="$server.user?.username"
            class="text-h6">
            {{ $server.user.username }}
          </div>
        </div>
      </div>
      <div
        v-if="$server.user?.email"
        class="row no-wrap q-pa-md">
        <div class="text-overline">
          {{ $server.user.email }}
        </div>
      </div>
      <QSeparator />
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
        <RouterLink
          v-slot="{ navigate }"
          to="/orders"
          custom>
          <QItem
            clickable
            @click="navigate()">
            <QItemSection>Mis incidencias</QItemSection>
          </QItem>
        </RouterLink>
        <QItem class="justify-center">
          <QBtn
            v-close-popup
            color="primary"
            label="Cerrar sesión"
            push
            size="sm"
            @click="$server.logoutUser" />
        </QItem>
      </QList>
    </QMenu>
  </QAvatar>
</template>

<script setup lang="ts">
</script>
