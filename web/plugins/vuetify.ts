const schefferTheme = {
  dark: false,
  colors: {
    background: '#fff',
    surface: '#FFFFFF',
    'surface-bright': '#FFFFFF',
    'surface-light': '#EEEEEE',
    'surface-variant': '#424242',
    'on-surface-variant': '#EEEEEE',
    primary: '#099F95',
    'primary-darken-1': '#099F95',
    secondary: '#80421F',
    'secondary-darken-1': '#80421F',
    error: '#f87171',
    info: '#313B36',
    success: '#4CAF50',
    warning: '#FB8C00',
  },
  variables: {
    'border-color': '#099F95',
    'border-opacity': 0.12,
    'high-emphasis-opacity': 0.87,
    'medium-emphasis-opacity': 0.60,
    'disabled-opacity': 0.38,
    'idle-opacity': 0.04,
    'hover-opacity': 0.04,
    'focus-opacity': 0.12,
    'selected-opacity': 0.08,
    'activated-opacity': 0.12,
    'pressed-opacity': 0.12,
    'dragged-opacity': 0.08,
    'theme-kbd': '#212529',
    'theme-on-kbd': '#FFFFFF',
    'theme-code': '#F5F5F5',
    'theme-on-code': '#000000',
  }
}

export default defineNuxtPlugin((nuxtApp) => {
  // check https://vuetify-nuxt-module.netlify.app/guide/nuxt-runtime-hooks.html
  nuxtApp.hook('vuetify:before-create', (options) => {
    options.vuetifyOptions.theme = {
      defaultTheme: 'schefferTheme',
      themes: {
        schefferTheme,
      },
    }
    if (import.meta.client) {
      console.log('vuetify:before-create', options)
    }
  })
})
