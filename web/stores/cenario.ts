import {defineStore} from "pinia";


export const cenarioStore = defineStore("cenario", () => {
    const {$api} = useNuxtApp();
    const loading = ref<boolean>(false);
    const lista = ref([])

    const load = async () => {
        loading.value = true;
        const { data } = await $api.get("/simulador/v1/cenarios/");
        lista.value = data.data;
        loading.value = false;
    }

    return {
        lista,
        loading,
        load
    }
})