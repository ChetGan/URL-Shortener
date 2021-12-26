# Frontend build with React
FROM node:16.3.0-alpine as build
RUN mkdir -p /app
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json package-lock.json /app/
RUN npm install
COPY . /app
#Exclude this command for production
RUN CI=true npm test
RUN npm run build

# Production Build with NGNIX
FROM nginx:1.20.2-alpine
COPY config/ngnix.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]