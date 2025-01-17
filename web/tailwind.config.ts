import type { Config } from "tailwindcss";
import twPrimeUI from "tailwindcss-primeui";

export default <Partial<Config>>{
  theme: {
    extend: {
      aspectRatio: {
        auto: "auto",
        square: "1 / 1",
        video: "16 / 9",
      },
    },
  },
  plugins: [twPrimeUI],
};
