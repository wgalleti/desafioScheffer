<template>
  <UContainer>
    <AppBar v-if="isLoggedIn" />
    <div class="flex-1 h-full relative flex flex-col">
      <div class="h-[calc(100vh-80px)]">
        <slot />
      </div>
    </div>
  </UContainer>
</template>
<script setup lang="ts">
const useAuth = authStore();
const isLoggedIn = computed(() => useAuth.isLoggedIn);
</script>
