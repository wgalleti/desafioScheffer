import { defineStore } from "pinia";

export const cenarioStore = defineStore("cenario", () => {
  const { $api } = useNuxtApp();
  const loading = ref(false);
  const lista = ref([]);
  const crudOperacoes = ref([]);
  const toast = useToast();

  const load = async () => {
    loading.value = true;
    const { data } = await $api.get("/simulador/v1/cenarios/?all");
    lista.value = data.data;
    loading.value = false;
  };

  const save = async (dados: any) => {
    loading.value = true;
    try {
      const { id, ...data } = dados;
      data.operacoes = crudOperacoes.value.map((v) => {
        delete v.pk;
        return {
          ...v,
          algodoeira: v.algodoeira.id,
          fazenda: v.fazenda.id,
        };
      });

      if (id) {
        await $api.patch(`/simulador/v1/cenarios/${id}/`, data);
      } else {
        await $api.post("/simulador/v1/cenarios/", data);
      }

      crudOperacoes.value = [];
      toast.add({
        severity: "success",
        summary: "Salvo",
        detail: "Cenário simulado com sucesso!",
        life: 3000,
      });
    } catch (e) {
      toast.add({
        severity: "error",
        summary: "Erro",
        detail: e.toString(),
        life: 3000,
      });
    } finally {
      loading.value = false;
    }
  };

  const addCrudOperacoes = (value) => {
    crudOperacoes.value.push(value);
  };

  const removeCrudOperacoes = (id) => {
    const idx = crudOperacoes.value.findIndex((v) => v.id === id);
    if (idx > -1) {
      crudOperacoes.value.splice(idx, 1);
    }
  };

  return {
    lista,
    loading,
    crudOperacoes,
    load,
    save,
    addCrudOperacoes,
    removeCrudOperacoes,
  };
});
