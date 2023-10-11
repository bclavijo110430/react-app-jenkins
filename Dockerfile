# Utiliza una imagen base de Node.js para construir la aplicación
FROM node:14 as build

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al directorio de trabajo
COPY . .


# Instala las dependencias
RUN npm install

# Construye la aplicación

RUN npm run build 

# Utiliza una imagen más ligera de Nginx para servir la aplicación
FROM nginx:alpine

# Copia los archivos generados en la etapa anterior a la carpeta de despliegue de Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expone el puerto 80
EXPOSE 80

# Inicia Nginx en segundo plano
CMD ["nginx", "-g", "daemon off;"]
