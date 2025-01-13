<script setup>
import { cenarioStore } from '@/stores/cenario.js'
import { computed, onMounted, ref } from 'vue'
import { algodoeiraStore } from '@/stores/algodoeira.js'
import { fazendaStore } from '@/stores/fazenda.js'
import { useToast } from 'primevue'
import { v4 as uuidv4 } from 'uuid'

const useAlgodoeira = algodoeiraStore()
const useFazenda = fazendaStore()
const useCenario = cenarioStore()

const operacoes = computed(() => useCenario.crudOperacoes)
const initialValues = ref({
  rolinhos: 0,
  fardoes: 0,
})
onMounted(() => {
  useAlgodoeira.load()
  useFazenda.load()
})
const algodoeiras = computed(() => useAlgodoeira.lista)
const fazendas = computed(() => useFazenda.lista)
const toast = useToast()

const loading = computed(() => useCenario.loading)

async function handleSave() {
  const data = { pk: uuidv4(), ...initialValues.value }
  useCenario.addCrudOperacoes(data)
  toast.add({
    severity: 'success',
    summary: 'Operação registrada',
    life: 2000,
  })
  setTimeout(() => {
    initialValues.value = {
      rolinhos: 0,
      fardoes: 0,
    }
  }, 100)
}

const resolver = ({ values }) => {
  const errors = {}
  if (!values.fazenda?.id) {
    errors.fazenda = [{ message: 'Fazenda é obrigatório' }]
  }

  if (!values.algodoeira?.id) {
    errors.algodoeira = [{ message: 'Algodoeira é obrigatório' }]
  }

  const { fardoes = 0, rolinhos = 0 } = values
  const total = fardoes + rolinhos
  if (total === 0) {
    errors.rolinhos = [{ message: 'É necessário ao menos um rolinho ou fardão' }]
  }

  return {
    errors,
  }
}
const submitForm = async (e) => {
  if (e.valid) {
    await handleSave(e)
    e.reset()
  }
}
</script>

<template>
  <Form
    v-slot="$form"
    :initialValues
    :resolver
    @submit="submitForm"
    class="grid grid-cols-3 gap-2 w-full"
  >
    <div>
      <label>Fazenda</label>
      <Select
        name="fazenda"
        v-model="initialValues.fazenda"
        :options="fazendas"
        option-label="nome"
        fluid
        show-clear
        autofocus
      />
      <Message v-if="$form.fazenda?.invalid" severity="error" size="small" variant="simple">{{
        $form.fazenda.error?.message
      }}</Message>
    </div>
    <div>
      <label>Algodoeira</label>
      <Select
        name="algodoeira"
        v-model="initialValues.algodoeira"
        :options="algodoeiras"
        option-label="nome"
        fluid
        show-clear
      />
      <Message v-if="$form.algodoeira?.invalid" severity="error" size="small" variant="simple">{{
        $form.algodoeira.error?.message
      }}</Message>
    </div>

    <div class="grid grid-cols-2 gap-2">
      <div>
        <label>Rolinhos</label>
        <InputNumber v-model="initialValues.rolinhos" name="rolinhos" :min="0" fluid />
      </div>

      <div>
        <label>Fardões</label>
        <InputNumber v-model="initialValues.fardoes" name="fardoes" :min="0" fluid />
      </div>
      <div class="col-span-2 gap-2">
        <Message v-if="$form.rolinhos?.invalid" severity="error" size="small" variant="simple">{{
          $form.rolinhos.error?.message
        }}</Message>
      </div>
    </div>

    <div class="col-span-3 w-full flex justify-end">
      <Button
        type="submit"
        label="Adicionar"
        severity="primary"
        icon="pi pi-plus"
        class="mb-8 w-28 place-self-end"
        :loading="loading"
      />
    </div>
    <div class="col-span-3 w-full">
      <DataTable v-if="operacoes.length" :value="operacoes" size="small">
        <Column field="fazenda.nome" header="Fazenda" />
        <Column field="algodoeira.nome" header="Algodoeira" />
        <Column field="rolinhos" header="Rolinhos" />
        <Column field="fardoes" header="Fardões" />
        <Column>
          <template #body="{ data }">
            <div class="flex flex-col gap-1">
              <Button
                icon="pi pi-trash"
                severity="danger"
                outlined
                @click="useCenario.removeCrudOperacoes(data.id)"
              />
            </div>
          </template>
        </Column>
      </DataTable>
    </div>
  </Form>
</template>
