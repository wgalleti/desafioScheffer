<script setup>
import CenarioForm from '@/components/CenarioForm.vue'
import { cenarioStore } from '@/stores/cenario.js'

const useCenario = cenarioStore()

function refresh() {
  useCenario.load()
}
</script>
<template>
  <div class="card">
    <Toolbar class="bg-primary rounded-none text-white">
      <template #end>
        <CenarioForm @update="refresh">
          <template #activator="{ openDialog }">
            <Button
              icon="pi pi-plus"
              class="mr-2 text-white hover:text-primary"
              severity="secondary"
              text
              @click="openDialog"
            />
          </template>
        </CenarioForm>

        <Button
          icon="pi pi-cloud-download"
          class="mr-2 text-white hover:text-primary"
          severity="secondary"
          text
        />
      </template>
    </Toolbar>
  </div>
</template>
