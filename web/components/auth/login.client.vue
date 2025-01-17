<script setup lang="ts">
import { object, string, type InferType } from "yup";
import type { FormSubmitEvent } from "#ui/types";

const useAuth = authStore();
const router = useRouter();
const toast = useToast();
const isLoggedIn = computed(() => useAuth.isLoggedIn);

const schema = object({
  username: string().required("Obrigatório"),
  password: string()
    .min(3, "Tem que ter pelo menos 3 caracteres")
    .required("Obrigatório"),
});

type Schema = InferType<typeof schema>;

const state = reactive({
  username: undefined,
  password: undefined,
});

async function onSubmit(event: FormSubmitEvent<Schema>) {
  try {
    await useAuth.login(event.data);
    if (isLoggedIn.value) {
      toast.add({ title: "Bem vindo!" });
      router.push("/");
    }
  } catch (error) {
    toast.add({ title: `Erro ao logar ${error.message}`, color: "red" });
  }
}
</script>

<template>
  <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
    <UFormGroup label="Usuário" name="username">
      <UInput v-model="state.username" autofocus />
    </UFormGroup>

    <UFormGroup label="Senha" name="password">
      <UInput v-model="state.password" type="password" />
    </UFormGroup>

    <UButton type="submit" block icon="mdi:account-lock-open" variant="outline"
      >Login</UButton
    >
  </UForm>
</template>
