/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#099F95",
        secondary: "#80421F",
        accent: "#099F95",
        text: "#313B36",
        contrast: "#CD950F",
        error: "#f87171",
        info: "#313B36",
        success: "#4CAF50",
        warning: "#FB8C00",
      }
    },
  },
  plugins: [],
  prefix: 'tw-',
}

