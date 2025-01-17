import { defineStore } from "pinia";

export const algodoeiraStore = defineStore("algodoeira", () => {
  const { $api } = useNuxtApp();
  const loading = ref(false);
  const lista = ref([]);

  const load = async () => {
    loading.value = true;
    const { data } = await $api.get("/base/v1/algodoeiras/");
    lista.value = data.data;
    loading.value = false;
  };

  return {
    lista,
    loading,
    load,
  };
});
