FROM node:alpine

EXPOSE 6969

ENV TARGET_HOST="127.0.0.1"
ENV TARGET_PORT="8080"

COPY . /proxy
WORKDIR /proxy
RUN yarn install
CMD ["yarn", "start"]