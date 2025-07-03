defmodule ApiWeb.ProcessController do
  use ApiWeb, :controller

  def index(conn, %{"data" => data}) do
    result = VacationSpot.process_data(data)
    json(conn, result)
  end
end