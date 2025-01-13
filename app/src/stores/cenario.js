import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import { ref } from 'vue'

export const cenarioStore = defineStore('cenario', () => {
  const loading = ref(false)
  const lista = ref([])

  const load = async () => {
    loading.value = true
    const { data } = await http.get('/simulador/v1/cenarios/')
    lista.value = data.data
    loading.value = false
  }

  return {
    lista,
    loading,
    load,
  }
})
