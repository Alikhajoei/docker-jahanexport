FROM node:20.18.0-slim as base

ENV NODE_ENV production

WORKDIR /usr/src/app

COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend .

RUN npm run build  
COPY --from=build /usr/src/app/.output /usr/src/app/.output
EXPOSE 3000

CMD [ "node", ".output/server/index.mjs" ]
