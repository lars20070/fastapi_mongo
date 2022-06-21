from fastapi import FastAPI

from app.server.routes.model import router as ModelRouter

app = FastAPI()

app.include_router(ModelRouter, tags=["Model"], prefix="/model")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Backend for Model Training Database."}
