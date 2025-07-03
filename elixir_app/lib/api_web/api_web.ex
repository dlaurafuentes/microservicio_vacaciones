defmodule ApiWeb do
  def controller do
    quote do
      use Phoenix.Controller, namespace: ApiWeb
    end
  end
end
