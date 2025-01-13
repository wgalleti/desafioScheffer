import { defineStore } from 'pinia'

import http from '@/plugins/axios'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'

export const authStore = defineStore(
  'auth',
  () => {
    const token = ref(null)
    const user = ref(null)
    const loading = ref(false)
    const isLoggedIn = computed(() => token.value && !!token.value)
    const router = useRouter()

    const check = async () => {
      try {
        loading.value = true
        const { data } = await http.get('auth/user/')
        user.value = data
      } catch {
        token.value = null
        user.value = null
      } finally {
        loading.value = false
      }
    }
    const login = async ({ username, password }) => {
      try {
        loading.value = true
        const { data } = await http.post('auth/login/', { username, password })
        const { token: accessToken, user: userInfo } = data

        token.value = accessToken
        user.value = userInfo
      } catch (e) {
        token.value = null
        user.value = null
        console.log(e)
      } finally {
        loading.value = false
      }
    }
    const logout = async () => {
      try {
        loading.value = true
        await http.post('auth/logout/')
      } catch {
        console.log('Faield user logged out')
      } finally {
        loading.value = false
        token.value = null
        user.value = null
        router.push('/login')
      }
    }

    return {
      token,
      user,
      isLoggedIn,
      loading,
      check,
      login,
      logout,
    }
  },
  {
    persist: true,
  },
)
