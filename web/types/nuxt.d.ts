import type { ToastService } from "primevue/toastservice";

declare module "nuxt/app" {
  interface NuxtApp {
    $api: typeof axios;
    $toast: ToastService;
  }
}
