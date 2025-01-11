<script setup>
const useApp = AppStore();
const useAuth = AuthStore();
const router = useRouter();

const valid = ref(false);
const visible = ref(false);
const form = ref({});
const isRequiredRule = ref([(v) => !!v || "Campo é obrigatório"]);
const loading = computed(() => useAuth.loading);

const version = computed(() => useApp.appVersion);

async function handleLogin() {
  if (!valid.value) {
    return;
  }
  await useAuth.login(form.value);
  if (useAuth.isLoggedIn) {
    router.push("/");
  }
}
</script>
<template>
  <v-container>
    <v-row no-gutters>
      <v-col align="center" justify="center">
        <div class="tw-w-[160px] tw-h-[40px] tw-p-2 tw-relative my-5">
          <div class="tw-bg-white/10 backdrop-blur tw-absolute tw-inset-0" />
          <img
            src="~/assets/img/cropped-logo-1.png"
            alt="Logo Scheffer"
            class="tw-w-[120px] tw-p-1"
          />
        </div>

        <h1 class="tw-text-2xl tw-text-contrast tw-font-extrabold">
          Desafio Técnico
        </h1>
        <h2 class="tw-text-xl tw-font-light">
          Distruibuição de produção de algodão
        </h2>
        <p
          class="tw-text-sm tw-text-contrast tw-font-light tw-tracking-tighter"
        >
          Versão {{ version }}
        </p>

        <v-form
          v-model="valid"
          class="tw-w-[280px] tw-mt-10"
          @submit.prevent="handleLogin"
        >
          <v-container fluid>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="form.username"
                  :rules="isRequiredRule"
                  label="Usuário"
                  required
                  autofocus
                />
              </v-col>
            </v-row>

            <v-text-field
              v-model="form.password"
              :rules="isRequiredRule"
              label="Senha"
              required
              :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
              :type="visible ? 'text' : 'password'"
              @click:append-inner="visible = !visible"
            />

            <v-btn
              class="mt-2"
              type="submit"
              block
              color="primary"
              :loading="loading"
              :disabled="!valid"
              >Entrar</v-btn
            >
          </v-container>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
