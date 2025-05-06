from fastapi import FastAPI
from database import engine
import models
from router import router

models.Base.metadata.creat_all(bind=engine)

app = FastAPI()
app.include_router(router)