FROM node:14-slim

WORKDIR /usr/src/client

COPY package*.json ./

RUN npm install

COPY next.config.js ./next.config.js

EXPOSE 3000

CMD ["npm", "run", "dev"]