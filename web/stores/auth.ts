import { defineStore } from "pinia";
import { useNuxtApp, useRouter } from "#app";

import type { iAuthCredenciais, iAuthResponse } from "~/types/stores/auth";
import { AppStore } from "~/stores/app";

export const AuthStore = defineStore(
  "auth",
  () => {
    const { $api } = useNuxtApp();

    const useApp = AppStore();

    const user = ref<string | null>(null);
    const token = ref<string | null>(null);
    const isLoggedIn = ref<boolean>(false);
    const loading = ref<boolean>(false);

    const login = async ({ username, password }: iAuthCredenciais) => {
      loading.value = true;

      try {
        const { data } = await $api.post<iAuthResponse>("auth/login/", {
          username,
          password,
        });

        const { token: authToken } = data;

        if (!token) {
          throw new Error("Token inválido");
        }

        user.value = username;
        token.value = authToken;
        isLoggedIn.value = true;
      } catch (e) {
        localStorage.clear();
        console.error(e);
      } finally {
        loading.value = false;
      }
    };

    const logout = async (redirect: boolean = true) => {
      const router = useRouter();

      user.value = null;
      token.value = null;
      isLoggedIn.value = false;

      if (redirect) {
        router.push("/login");
      }
    };

    const check = async () => {
      try {
        useApp.showLoading("Verificando login...");
        const { data } = await $api.get<iAuthResponse>("auth/user/");
        user.value = data;
        isLoggedIn.value = true;
      } catch (e) {
        console.error(e);
        await logout(false);
      } finally {
        useApp.closeLoading();
      }
    };

    return {
      user,
      token,
      isLoggedIn,
      loading,
      login,
      logout,
      check,
    };
  },
  {
    persist: true,
  }
);
