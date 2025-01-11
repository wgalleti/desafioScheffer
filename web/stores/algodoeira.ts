import {defineStore} from "pinia";
import type {iAlgodoeiraDados, iAlgodoeiraResponse} from "~/types/stores/algodoeira";

export const algodoeiraStore = defineStore("algodoeira", () => {
    const {$api} = useNuxtApp();
    const loading = ref<boolean>(false);
    const lista = ref<iAlgodoeiraDados[]>([])

    const load = async () => {
        loading.value = true;
        const { data } = await $api.get<iAlgodoeiraResponse>("/base/v1/algodoeiras/");
        lista.value = data.data;
        loading.value = false;
    }

    return {
        lista,
        loading,
        load
    }
})