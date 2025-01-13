import '@/assets/css/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'
import AnimateOnScroll from 'primevue/animateonscroll'

import App from '@/App.vue'
import router from '@/router'

import locale from '@/plugins/primevue/locale'
import { SchefferPreset } from '@/theme/default'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const app = createApp(App)

app.use(PrimeVue, {
  theme: {
    locale,
    preset: SchefferPreset,
    options: {
      darkModeSelector: false,
      cssLayer: {
        name: 'primevue',
        order: 'tailwind-base, primevue, tailwind-utilities',
      },
    },
  },
})
app.use(ToastService)
app.directive('animateonscroll', AnimateOnScroll)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)

app.mount('#app')
