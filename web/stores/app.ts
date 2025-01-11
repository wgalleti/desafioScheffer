import { defineStore } from "pinia";

export const AppStore = defineStore(
  "app",
  () => {
    const appVersion = ref<string>("1.0.0");
    const loading = ref<boolean>(false);
    const loadingText = ref<string | null>(null);

    const showLoading = (text: string | null) => {
      loading.value = true;
      loadingText.value = text;
    };
    const closeLoading = () => {
      loading.value = false;
      loadingText.value = null;
    };

    return {
      appVersion,
      loading,
      showLoading,
      closeLoading,
    };
  },
  {
    persist: true,
  }
);
