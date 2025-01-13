<script setup>
import LayoutNav from '@/components/layout/Nav.vue'
import { authStore } from '@/stores/auth.js'
import { computed } from 'vue'
const useAuth = authStore()
const isLoggedIn = computed(() => useAuth.isLoggedIn)
</script>

<template>
  <div class="h-full w-full">
    <Toast />
    <LayoutNav v-if="isLoggedIn" />
    <div>
      <RouterView />
    </div>
  </div>
</template>
