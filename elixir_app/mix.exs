defmodule VacationSpot.MixProject do
use Mix.Project
def project do
[
app: :vacation_spot,
version: 0.1.0,
elixir: ~> 1.14,
]
end
def application do
[
extra_applications: [:logger]
]
end
defp deps do
[
{:plug_cowboy, ~> 2.5}
]
end
end
