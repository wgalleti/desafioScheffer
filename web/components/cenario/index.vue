<template>
  <div class="card">
    <DataTable :value="cenarios" tableStyle="min-width: 50rem">
      <Column field="nome" header="Nome"></Column>
      <Column field="inicio" header="Inicio"></Column>
      <Column field="termino" header="Termino"></Column>
      <Column field="dias" header="Dias"></Column>
      <Column header="Fardos" class="w-max">
        <template #body="{ data }">
          <div class="flex gap-2">
            <div class="flex flex-col items-center border p-2 rounded-md">
              <small class="text-xs font-thin mb-2">Fardões</small>
              <i class="pi pi-expand text-primary" style="font-size: 3rem"></i>
              <p class="text-2xl font-thin tracking-tighter">
                {{ data.fardoes }}
              </p>
            </div>
            <div class="flex flex-col items-center border p-2 rounded-md">
              <small class="text-xs font-thin mb-2">Rolinhos</small>
              <i class="pi pi-circle text-primary" style="font-size: 3rem"></i>
              <p class="text-2xl font-thin tracking-tighter">
                {{ data.rolinhos }}
              </p>
            </div>
            <div class="flex flex-col items-center border p-2 rounded-md">
              <small class="text-xs font-thin mb-2">Produção</small>
              <i class="pi pi-barcode text-primary" style="font-size: 3rem"></i>
              <p class="text-2xl font-thin tracking-tighter">
                {{ data.total_fardos }}
              </p>
            </div>
          </div>
        </template>
      </Column>
      <Column class="w-4 !text-end">
        <template #body="{ data }">
          <div class="flex flex-col gap-1">
            <Button icon="pi pi-search" severity="secondary" outlined></Button>
            <Button icon="pi pi-pencil" severity="info" outlined></Button>
            <Button icon="pi pi-trash" severity="danger" outlined></Button>
          </div>
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<script setup>
defineProps({
  cenarios: {
    type: Array,
    required: true,
    default: () => [],
  },
});
</script>
