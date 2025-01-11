import {defineStore} from "pinia";
import type {iFazendaDados, iFazendaResponse} from "~/types/stores/fazenda";

export const fazendaStore = defineStore("fazenda", () => {
    const {$api} = useNuxtApp();
    const loading = ref<boolean>(false);
    const lista = ref<iFazendaDados[]>([])

    const load = async () => {
        loading.value = true;
        const { data } = await $api.get<iFazendaResponse>("/base/v1/fazendas/");
        lista.value = data.data;
        loading.value = false;
    }

    return {
        lista,
        loading,
        load
    }
})