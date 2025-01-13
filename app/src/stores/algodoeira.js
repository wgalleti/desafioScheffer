import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import { ref } from 'vue'

export const algodoeiraStore = defineStore('algodoeira', () => {
  const loading = ref(false)
  const lista = ref([])

  const load = async () => {
    loading.value = true
    const { data } = await http.get('/base/v1/algodoeiras/')
    lista.value = data.data
    loading.value = false
  }

  return {
    lista,
    loading,
    load,
  }
})
