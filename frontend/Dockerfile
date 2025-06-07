FROM node:22-alpine

ENV NEXT_TELEMETRY_DISABLED=1

WORKDIR /app

# Copiar el package.json y package-lock.json
COPY cuestionario-ia/package*.json ./
RUN npm install

# Copiar el resto de la aplicación
COPY cuestionario-ia/ .

CMD ["npm", "run", "dev"]