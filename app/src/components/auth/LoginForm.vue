<script setup>
import { useRouter } from 'vue-router'
import { authStore } from '@/stores/auth.js'
import { computed, ref } from 'vue'

const useAuth = authStore()
const router = useRouter()

const loading = computed(() => useAuth.loading)
const isLoggedIn = computed(() => useAuth.isLoggedIn)

async function handleLogin() {
  const { username, password } = initialValues.value
  await useAuth.login({ username, password })

  if (isLoggedIn.value) {
    router.push('/')
  }
}

const initialValues = ref({
  username: '',
  password: '',
})

const resolver = ({ values }) => {
  const errors = {}

  if (!values.username) {
    errors.username = [{ message: 'Usuario é obrigatório' }]
  }

  if (!values.password) {
    errors.password = [{ message: 'Senha é obrigatório' }]
  }

  return {
    errors,
  }
}
const submitForm = async (e) => {
  if (e.valid) {
    await handleLogin()
    e.reset()
  }
}
</script>

<template>
  <Form
    v-slot="$form"
    :initial-values="initialValues"
    :resolver
    @submit="submitForm"
    class="grid gap-2 w-full"
  >
    <div>
      <label>Usuário</label>
      <InputText v-model="initialValues.username" name="username" type="text" fluid autofocus />
      <Message v-if="$form.username?.invalid" severity="error" size="small" variant="simple">{{
        $form.username.error?.message
      }}</Message>
    </div>
    <div>
      <label>Senha</label>
      <InputText v-model="initialValues.password" name="password" type="password" fluid />
      <Message v-if="$form.password?.invalid" severity="error" size="small" variant="simple">{{
        $form.password.error?.message
      }}</Message>
    </div>
    <Button
      type="submit"
      severity="primary"
      label="Entrar"
      icon="pi pi-lock"
      class="mt-8"
      :loading="loading"
    />
  </Form>
</template>
