from fastapi import APIRouter
from .predict import predict_router

api_router = APIRouter()
#api_router.include_router(predict_router, prefix="/recommend", tags=["recommend"])
api_router.include_router(predict_router, tags=["recommend"])