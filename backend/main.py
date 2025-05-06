from fastapi import FastAPI
from backend.database import engine
import models
from router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)