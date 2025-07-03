FROM elixir:1.14.3-alpine
WORKDIR /app

# Instala herramientas necesarias
RUN apk add --no-cache build-base git && \
    mix local.hex --force && \
    mix local.rebar --force

# Copia solo los archivos de dependencias primero (para cachear)
COPY mix.exs mix.lock ./
RUN mix deps.get && mix deps.compile

# Copia el resto de la aplicación
COPY . .

CMD ["mix", "phx.server"]