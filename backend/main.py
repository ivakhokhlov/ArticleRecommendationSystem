from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.router import api_router


def get_app() -> FastAPI:
    """
    FastAPI app initialization.
    """
    fastapi_app = FastAPI(
        title="Recommendation Service",
        version="0.1.0",
        debug=True,
        description="ML service for recommending articles",
    )
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )
    fastapi_app.include_router(api_router)
    return fastapi_app


app = get_app()

""" if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) """
