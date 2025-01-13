<script setup>
import { cenarioStore } from '@/stores/cenario.js'
import { computed, ref } from 'vue'
import CenarioFormOperacoes from '@/components/CenarioFormOperacoes.vue'

const useCenario = cenarioStore()
const loading = computed(() => useCenario.loading)
const initialValues = ref({
  inicio: new Date(),
})
const dialog = ref(false)

defineEmits(['update'])

async function handleSave() {
  const data = { ...initialValues.value }
  data['inicio'] = data['inicio'].toISOString().split('T')[0]
  await useCenario.save(data)
  initialValues.value = {
    inicio: new Date(),
  }
  dialog.value = false
}

const resolver = ({ values }) => {
  const errors = {}

  if (!values.inicio) {
    errors.inicio = [{ message: 'Inicio é obrigatório' }]
  }

  if (!values.nome) {
    errors.nome = [{ message: 'Nome é obrigatório' }]
  }

  return {
    errors,
  }
}

const submitForm = async (e) => {
  if (e.valid) {
    await handleSave()
    e.reset()
  }
}

function openDialog() {
  dialog.value = true
}
</script>

<template>
  <slot name="activator" :open-dialog="openDialog"></slot>
  <Dialog
    header=" "
    v-model:visible="dialog"
    position="top"
    modal
    :draggable="false"
    style="width: 750px"
    @hide="$emit('update')"
  >
    <Form
      v-slot="$form"
      :initial-values="initialValues"
      :resolver
      @submit="submitForm"
      class="grid grid-cols-2 gap-2 w-full"
    >
      <div class="col-span-2 w-full mt-10">
        <h1 class="text-primary text-2xl border-b pb-2 mb-4">Cenário</h1>
      </div>
      <div>
        <label>Nome</label>
        <InputText v-model="initialValues.nome" name="nome" type="text" fluid autofocus />
        <Message v-if="$form.nome?.invalid" severity="error" size="small" variant="simple">{{
          $form.nome.error?.message
        }}</Message>
      </div>
      <div>
        <label>Inicio</label>
        <DatePicker
          name="inicio"
          v-model="initialValues.inicio"
          show-button-bar
          hour-format="24"
          date-format="dd/mm/yy"
          :min-date="new Date()"
          show-icon
          show-on-focus
          fluid
        />
        <Message v-if="$form.inicio?.invalid" severity="error" size="small" variant="simple">{{
          $form.inicio.error?.message
        }}</Message>
      </div>
      <div class="col-span-2 w-full mt-10">
        <h1 class="text-primary text-2xl border-b pb-2 mb-4">Operações</h1>
        <CenarioFormOperacoes />
      </div>
      <div class="col-span-2 w-full flex flex-col justify-end">
        <h1 class="text-primary text-2xl border-b pb-2 mb-4">Finalizar</h1>
        <Button
          type="submit"
          severity="primary"
          label="Simular"
          icon="pi pi-chart-scatter"
          class="w-28 self-end"
          :loading="loading"
        />
      </div>
    </Form>
  </Dialog>
</template>
