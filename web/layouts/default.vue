<script setup>
const useAuth = AuthStore();
const isLoggedIn = computed(() => useAuth.isLoggedIn);
</script>
<template>
  <v-app>
    <v-main
      class="tw-bg-gradient-to-bl tw-from-secondary tw-to-contrast tw-text-white"
    >
      <v-app-bar v-if="isLoggedIn" app flat density="compact" color="secondary">
        <template #prepend>
          <v-img
            src="~/assets/img/cropped-logo-1.png"
            alt="Logo Scheffer"
            class="tw-w-[120px] tw-ml-2"
          />
        </template>
        <v-spacer />
        <v-btn icon color="primary" size="small" @click="useAuth.logout">
          <v-icon>mdi-logout</v-icon>
        </v-btn>
      </v-app-bar>
      <slot />
    </v-main>
  </v-app>
</template>
