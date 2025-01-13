/** @type {import('tailwindcss').Config} */
import twPrimeUi from 'tailwindcss-primeui'

export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      container: {
        center: true,
      },
    },
  },
  plugins: [twPrimeUi],
}
