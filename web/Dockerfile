FROM node:lts-alpine AS build
WORKDIR /app
COPY package*.json yarn.lock ./
RUN yarn
COPY . .
ENV NODE_OPTIONS="--max-old-space-size=8192"
RUN yarn build

FROM node:lts-alpine AS worker
WORKDIR /app
RUN yarn global add pm2
COPY --from=build /app/.output /app
EXPOSE 3000
CMD ["pm2-runtime", "start", "./server/index.mjs"]