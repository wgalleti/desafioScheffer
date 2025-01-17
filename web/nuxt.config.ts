// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },
  ssr: false,
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.API_BASE_URL || "http://localhost:8000/api",
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
  modules: [
    "@pinia/nuxt",
    "pinia-plugin-persistedstate/nuxt",
    "@nuxt/eslint",
    "nuxt-svgo",
    "nuxt-lodash",
    "@nuxt/icon",
    "@hebilicious/vue-query-nuxt",
    "@nuxt/ui",
  ],
  ui: {
    global: true,
  },
  colorMode: {
    preference: "light",
  },
});
