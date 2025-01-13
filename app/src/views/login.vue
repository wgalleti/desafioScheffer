<script setup>
import LoginForm from '@/components/auth/LoginForm.vue'
</script>

<template>
  <div
    class="min-h-screen w-full md:justify-end flex gap-2 transition-all duration-500 bg-gradient-to-r from-primary to-white"
  >
    <div
      class="animate-fade w-full md:w-[280px] p-4 flex flex-col items-center justify-center backdrop-blur-lg border-l border-primary-50"
    >
      <div class="bg-white/20 p-4 rounded my-7">
        <img
          src="/logo.png"
          alt="Logo"
          class="object-contain hover:scale-110 duration-500 transition"
        />
      </div>

      <LoginForm />
    </div>
  </div>
</template>
