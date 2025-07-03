from fastapi import FastAPI
from services.recommender import VacationSpotRecommender
import httpx

app = FastAPI()

@app.get("/recommend")
async def recommend_spot(bbox: str, start_date: str, end_date: str):
    recommender = VacationSpotRecommender(start_date, end_date)
    recommendations = await recommender.recommend(bbox)
    return {
        "bbox": bbox,
        "date_range": [start_date, end_date],
        "recommendations": recommendations
    }
