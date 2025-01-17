import axios from "axios";
export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig();

  const defaultUrl = String(config.public.apiBaseUrl);

  const api = axios.create({
    baseURL: defaultUrl,
  });

  api.interceptors.request.use((config) => {
    const auth = localStorage.getItem("auth");
    if (!auth) {
      return config;
    }
    const { token } = JSON.parse(auth);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  });
  return {
    provide: {
      api: api,
    },
  };
});
