export default defineNuxtRouteMiddleware(async (to) => {
  const useAuth = AuthStore();
  await useAuth.check();

  // Check if route is login
  if (!useAuth.isLoggedIn && to.path === "/login") {
    return;
  }

  if (!useAuth.isLoggedIn && to.path !== "/login") {
    await useAuth.logout();
    return navigateTo("/login");
  }

  // Check if is not authenticated and redirect to login
  if (!useAuth.isLoggedIn) {
    return navigateTo("/login");
  }

  if (useAuth.isLoggedIn && to.path === "/login") {
    return navigateTo("/");
  }

  return;
});
