from fastapi import APIRouter, HTTPException
from src.schemas.requests import QueryRequest
from src.services.model import get_recommendations

predict_router = APIRouter()

@predict_router.post("/recommend/")
async def recommend(request: QueryRequest):
    user_input = request.query
    if not user_input:
        raise HTTPException(status_code=400, detail="Запрос не может быть пустым")

    recommendations = get_recommendations(user_input)
    return {"recommendations": recommendations} # recommendations
