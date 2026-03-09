from fastapi import FastAPI
from routers import users
from routers import ai
from database import engine
import models

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ArogyaMitra API",
    description="AI Healthcare Assistant Backend",
    version="1.0"
)

# CORS configuration
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "ArogyaMitra API running"}

app.include_router(users.router)
app.include_router(ai.router)