<template>
  <div class="w-full h-full">
    <AppNav v-if="isLoggedIn" />
    <div class="flex-1 h-full relative flex flex-col">
      <div class="h-[calc(100vh-80px)]">
        <slot />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
const useAuth = authStore();
const isLoggedIn = computed(() => useAuth.isLoggedIn);
</script>
