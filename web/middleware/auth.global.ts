export default defineNuxtRouteMiddleware(async (to) => {
  const useAuth = authStore();

  // Check if route is login
  if (to.path === "/login") {
    return;
  }

  await useAuth.check();

  // Check if is authenticated
  if (useAuth.isLoggedIn) {
    return;
  }

  // Check if is not authenticated and redirect to login
  if (!useAuth.isLoggedIn) {
    return navigateTo("/login");
  }
});
