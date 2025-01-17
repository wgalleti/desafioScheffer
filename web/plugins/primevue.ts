import { defineNuxtPlugin } from "#app";
import PrimeVue from "primevue/config";
import ToastService from "primevue/toastservice";
import ConfirmationService from "primevue/confirmationservice";

/* eslint-disable @typescript-eslint/no-explicit-any */
export default defineNuxtPlugin((nuxtApp: any) => {
  nuxtApp.vueApp.use(PrimeVue);
  nuxtApp.vueApp.use(ToastService);
  nuxtApp.vueApp.use(ConfirmationService);

  return {
    provide: {
      toast: nuxtApp.vueApp.config.globalProperties
        .$toast as typeof ToastService,
      confirm: nuxtApp.vueApp.config.globalProperties
        .$confirm as typeof ConfirmationService,
    },
  };
});
