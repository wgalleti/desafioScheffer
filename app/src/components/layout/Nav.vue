<script setup lang="ts">
import { computed, ref } from 'vue'
import { authStore } from '@/stores/auth.js'

const useAuth = authStore()

const picture = computed(() => useAuth?.user?.picture || '/default-user.svg')

const items = ref([
  // {
  //   label: 'Dashboard',
  //   icon: 'pi pi-home'
  // },
  // {
  //   label: 'Cadastros',
  //   icon: 'pi pi-search',
  //   items: [
  //     {
  //       label: 'Test',
  //       icon: 'pi pi-bolt'
  //     }
  //   ]
  // },
  // {
  //   label: 'Protocolos',
  //   icon: 'pi pi-check',
  //   items: [
  //     {
  //       label: 'Criar',
  //       icon: 'pi pi-bolt'
  //     },
  //     {
  //       label: 'Receber',
  //       icon: 'pi pi-bolt'
  //     },
  //     {
  //       label: 'Recusar',
  //       icon: 'pi pi-bolt'
  //     }
  //   ]
  // }
])
</script>

<template>
  <Menubar :model="items" class="w-full">
    <template #start>
      <img
        src="/logo.png"
        alt="Logo"
        class="object-contain hover:scale-110 duration-500 transition h-6"
      />
    </template>
    <template #item="{ item, props, hasSubmenu, root }">
      <a v-ripple class="flex items-center" v-bind="props.action">
        <span>{{ item.label }}</span>
        <Badge v-if="item.badge" :class="{ 'ml-auto': !root, 'ml-2': root }" :value="item.badge" />
        <span
          v-if="item.shortcut"
          class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1"
          >{{ item.shortcut }}</span
        >
        <i
          v-if="hasSubmenu"
          :class="['pi pi-angle-down ml-auto', { 'pi-angle-down': root, 'pi-angle-right': !root }]"
        ></i>
      </a>
    </template>
    <template #end>
      <div class="flex items-center gap-2">
        <Avatar :image="picture" shape="circle" size="large" />
        <Button icon="pi pi-times" text @click="useAuth.logout()" severity="danger" />
      </div>
    </template>
  </Menubar>
</template>
