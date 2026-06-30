from fastapi import FastAPI
from app.api.routes import scheduler

app = FastAPI(title="Vehicle Maintenance Scheduler API")

app.include_router(scheduler.router,prefix="/api/v1")

@app.get("/health")
def health():
    return {"status":"OKAY"}