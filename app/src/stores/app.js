import { defineStore } from 'pinia'
import { ref } from 'vue'

export const appStore = defineStore('app', () => {
  const version = ref('1.0')

  return {
    version,
  }
})
