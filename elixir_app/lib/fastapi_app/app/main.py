from fastapi import FastAPI
from services.recommender import VacationSpotRecommender
import httpx

app = FastAPI()

@app.get("/recommend")
async def recommend_spot(bbox: str, start_date: str, end_date: str):
    recommender = VacationSpotRecommender(start_date, end_date)
    return await recommender.recommend(bbox)

# Opcional: Integración con Elixir
@app.get("/elixir-process/{data}")
async def elixir_process(data: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://elixir_app:4000/api/process?data={data}")
        return response.json()