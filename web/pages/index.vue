<script setup>
const useAlgodoeira = algodoeiraStore();
const useFazenda = fazendaStore();
const useCenario = cenarioStore();

const algodoeiras = computed(() => useAlgodoeira.lista);
const fazendas = computed(() => useFazenda.lista);
const cenarios = computed(() => useCenario.lista);

onMounted(() => {
  useAlgodoeira.load();
  useFazenda.load();
  useCenario.load();
});
</script>
<template>
  <main class="grid grid-cols-12 mt-6 p-2 gap-3">
    <div class="col-span-2 border rounded-lg p-2">
      <h1 class="text-3xl font-thin text-center my-2 text-primary-950">
        Algodoeiras
      </h1>
      <ul class="my-2">
        <li
          v-for="algodoeira in algodoeiras"
          :key="algodoeira.id"
          class="text-base py-1 border-l-2 pl-2 border-primary mb-1 hover:border-l-8 transition-all duration-500"
        >
          <div class="flex justify-between">
            <h2>{{ algodoeira.nome }}</h2>
            <p class="text-primary-950 font-thin tracking-tighter">
              {{ algodoeira.producao }}
            </p>
          </div>
        </li>
      </ul>

      <h1 class="text-3xl font-thin text-center my-2 text-primary-950">
        Fazendas
      </h1>
      <ul class="my-2">
        <li
          v-for="fazenda in fazendas"
          :key="fazenda.id"
          class="text-base py-1 border-l-2 pl-2 border-primary mb-1 hover:border-l-8 transition-all duration-500"
        >
          <div class="flex justify-between flex flex-col">
            <h2>{{ fazenda.nome }}</h2>
            <div
              class="text-primary-950 font-thin tracking-tighter flex justify-between px-1"
            >
              <p>
                {{ fazenda.rolinhos }}<span class="text-xs"> Rolinhos</span>
              </p>
              <p>{{ fazenda.fardoes }}<span class="text-xs"> Fardões</span></p>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div class="col-span-10 border rounded-lg p-2">
      <CenarioNav />
      <Cenario :cenarios="cenarios" />
    </div>
  </main>
</template>
