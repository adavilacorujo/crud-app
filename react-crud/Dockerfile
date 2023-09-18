# Specify a base image
FROM node:alpine as builder

WORKDIR /app

# Install some depenendencies
COPY package.json /app
RUN yarn install
COPY . .
RUN yarn build

# FROM nginx:latest
# WORKDIR /usr/share/nginx/html
# RUN rm -rf ./*
# COPY --from=builder /app/build .

EXPOSE 3000

ENTRYPOINT [ "yarn", "start" ]
# ENTRYPOINT [ "nginx", "-g", "daemon off;" ]