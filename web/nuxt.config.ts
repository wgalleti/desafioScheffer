// https://nuxt.com/docs/api/configuration/nuxt-config
import Aura from "@primevue/themes/aura";
import { definePreset } from "@primevue/themes";

const Theme = definePreset(Aura, {
  semantic: {
    primary: {
      50: "{emerald.50}",
      100: "{emerald.100}",
      200: "{emerald.200}",
      300: "{emerald.300}",
      400: "{emerald.400}",
      500: "{emerald.500}",
      600: "{emerald.600}",
      700: "{emerald.700}",
      800: "{emerald.800}",
      900: "{emerald.900}",
      950: "{emerald.950}",
    },
  },
});

export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },
  ssr: false,
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.API_BASE_URL || "http://localhost:8000/api",
    },
  },
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          api: "modern-compiler",
        },
      },
    },
  },
  svgo: {
    defaultImport: "component",
  },
  css: ["~/assets/scss/main.scss"],
  primevue: {
    options: {
      locale: {
        accept: "Aceitar",
        reject: "Rejeitar",
        firstDayOfWeek: 1,
        dayNames: [
          "Domingo",
          "Segunda-feira",
          "Terça-feira",
          "Quarta-feira",
          "Quinta-feira",
          "Sexta-feira",
          "Sábado",
        ],
        dayNamesShort: ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"],
        dayNamesMin: ["D", "S", "T", "Q", "Q", "S", "S"],
        monthNames: [
          "Janeiro",
          "Fevereiro",
          "Março",
          "Abril",
          "Maio",
          "Junho",
          "Julho",
          "Agosto",
          "Setembro",
          "Outubro",
          "Novembro",
          "Dezembro",
        ],
        monthNamesShort: [
          "Jan",
          "Fev",
          "Mar",
          "Abr",
          "Mai",
          "Jun",
          "Jul",
          "Ago",
          "Set",
          "Out",
          "Nov",
          "Dez",
        ],
        today: "Hoje",
        clear: "Limpar",
      },
      theme: {
        preset: Theme,
        options: {
          darkModeSelector: false,
        },
      },
    },
  },
  app: {
    head: {
      title: "Desafio Scheffer",
      bodyAttrs: {
        class: "h-full w-full dx-viewport",
      },
      htmlAttrs: {
        class: "h-full w-full scroll-smooth",
      },
    },
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  icon: {
    serverBundle: {
      collections: ["uil", "mdi"],
    },
  },
  piniaPluginPersistedstate: {
    storage: "localStorage",
  },
  modules: [
    "@pinia/nuxt",
    "pinia-plugin-persistedstate/nuxt",
    "@nuxt/eslint",
    "nuxt-svgo",
    "nuxt-lodash",
    "@hebilicious/vue-query-nuxt",
    "@primevue/nuxt-module",
    "@nuxtjs/tailwindcss",
    "@nuxt/icon",
  ],
});
