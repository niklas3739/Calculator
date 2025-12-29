from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="Calculator API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api")
