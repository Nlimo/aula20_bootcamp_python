from fastapi import FastAPI
from backend.database import engine
from backend import models
from backend.router import router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)