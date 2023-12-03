<template>
  <QLayout>
    <QHeader elevated>
      <QToolbar>
        <RouterLink
          v-slot="{ navigate }"
          to="/"
          custom>
          <QToolbarTitle
            class="cursor-pointer"
            @click="navigate">
            <QAvatar>
              <img src="/logo.png" />
            </QAvatar>
            TrainerBook
          </QToolbarTitle>
        </RouterLink>
      </QToolbar>
    </QHeader>

    <QPageContainer>
      <PageView />
    </QPageContainer>
  </QLayout>
</template>

<script setup lang="ts">
</script>
