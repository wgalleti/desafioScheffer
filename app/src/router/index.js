import { createRouter, createWebHistory } from 'vue-router'
import authGuard from '@/router/guard.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login.vue'),
    },
    {
      path: '/',
      name: 'home',
      component: () => import('../views/index.vue'),
    },
  ],
})

router.beforeEach(authGuard)

export default router
