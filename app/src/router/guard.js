import { authStore } from '@/stores/auth.js'
import { computed } from 'vue'

const authGuard = async (to) => {
  const useAuth = authStore()
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  await useAuth.check()
  const isLoggedIn = computed(() => useAuth.isLoggedIn)

  if (authRequired && !isLoggedIn.value) {
    return '/login'
  }

  if (isLoggedIn.value) {
    if (to.path === '/login') {
      return '/'
    }
  }
}

export default authGuard
