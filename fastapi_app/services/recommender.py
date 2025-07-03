import httpx
import random
from datetime import datetime
from typing import List, Dict, Any

class VacationSpotRecommender:
    OSM_OVERPASS_URL = "https://overpass-api.de/api/interpreter"

    def __init__(self, start_date: str, end_date: str, min_rating: float = 3.5):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.min_rating = min_rating

    async def fetch_tourist_spots(self, bbox: str) -> List[Dict[str, Any]]:
        query = f"""
            [out:json];
            (
                node["tourism"~"attraction|hotel|beach"]["name"]({bbox});
                way["tourism"~"attraction|hotel|beach"]["name"]({bbox});
            );
            out center;
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(self.OSM_OVERPASS_URL, params={"data": query})
            return response.json().get("elements", [])

    def filter_by_traffic(self, spots: List[Dict], max_crowding: float = 0.7) -> List[Dict]:
        return [spot for spot in spots if random.uniform(0.1, 1.0) <= max_crowding]

    def add_plus_factors(self, spots: List[Dict]) -> List[Dict]:
        return [
            {
                **spot,
                "weather_score": random.uniform(0.8, 1.0),
                "safety_score": random.uniform(0.7, 1.0),
                "nearby_services": random.sample(["restaurant", "hospital", "transport"], 2)
            }
            for spot in spots
        ]

    async def recommend(self, bbox: str) -> List[Dict]:
        spots = await self.fetch_tourist_spots(bbox)
        uncrowded_spots = self.filter_by_traffic(spots)
        return sorted(
            self.add_plus_factors(uncrowded_spots),
            key=lambda x: -x["weather_score"]
        )[:5]