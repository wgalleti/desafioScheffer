declare module "nuxt/app" {
  interface NuxtApp {
    $api: typeof axios;
  }
}
