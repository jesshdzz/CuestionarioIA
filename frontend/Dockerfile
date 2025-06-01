FROM node:22-slim

ENV NEXT_TELEMETRY_DISABLED=1
WORKDIR /app

# Copiar el package.json y package-lock.json
COPY cuestionario-ia/package*.json ./
RUN npm install

# Copiar el resto de la aplicación
COPY cuestionario-ia/ .
EXPOSE 3000

CMD ["npm", "run", "dev"]