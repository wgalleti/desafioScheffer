export const appStore = defineStore(
  "app",
  () => {
    const currentVersion = ref<string>("1.0");
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

    // LAYOUT
    const sideMenu = ref<boolean>(false);

    return {
      currentVersion,
      loading,
      loadingText,
      showLoading,
      closeLoading,
      sideMenu,
    };
  },
  {
    persist: true,
  },
);
