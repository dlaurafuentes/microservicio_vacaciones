FROM elixir:1.14.3-alpine
WORKDIR /app
mix local.rebar --force
COPY mix.exs mix.lock ./
RUN mix deps.get
COPY . .
CMD [mix, phx.server]
