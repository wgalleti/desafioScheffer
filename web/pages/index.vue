<script lang="ts" setup>

import {cenarioStore} from "~/stores/cenario";

const useFazenda = fazendaStore()
const useAlgodoeira = algodoeiraStore()
const useCenario = cenarioStore()

const fazendas = computed(() => useFazenda.lista)
const algodoeiras = computed(() => useAlgodoeira.lista)
const cenarios = computed(() => useCenario.lista)

const itemsPerPage = ref(5);
const headers = ref([
  {
    title: 'Nome',
    align: 'start',
    sortable: false,
    key: 'nome',
  },
  { title: 'Inicio', key: 'inicio', align: 'center' },
  { title: 'Termino', key: 'Termino', align: 'center' },
  { title: 'Dias', key: 'dias', align: 'end' },
  { title: 'Fardões', key: 'fardoes', align: 'end' },
  { title: 'Rolinhos', key: 'rolinhos', align: 'end' },
  { title: 'Total de Fardos', key: 'total_fardos', align: 'end' },
])
const search = ref('')

const loading = computed(() => useCenario.loading)
const totalItems = computed(() => cenarios.value.length)
onMounted(() => {
  useFazenda.load()
  useAlgodoeira.load()
  useCenario.load()
})
</script>

<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="3">
        <v-list lines="two" density="compact" class="tw-rounded" bg-color="secondary">
          <v-list-subheader>Fazendas</v-list-subheader>
          <v-list-item
              v-for="fazenda in fazendas"
              :key="fazenda.id"
              :title="fazenda.nome"
              class="tw-text-xs"
              :subtitle="`Fardoes: ${fazenda.fardoes}, Fardinhos: ${fazenda.rolinhos}`"
          />
          <v-list-subheader>Algodoeiras</v-list-subheader>
          <v-list-item
              v-for="algodoeira in algodoeiras"
              :key="algodoeira.id"
              :title="algodoeira.nome"
              class="tw-text-xs"
              :subtitle="`Produção: ${algodoeira.producao}`"
          />
        </v-list>
      </v-col>
      <v-col cols="9">
        <div class="tw-p-5">
          <h2>Cenários</h2>
          <v-data-table-server
              v-model:items-per-page="itemsPerPage"
              :headers="headers"
              :items="cenarios"
              :items-length="totalItems"
              :loading="loading"
              :search="search"
              item-value="name"
              @update:options="loadItems"
          />
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
