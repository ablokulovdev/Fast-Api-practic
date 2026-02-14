from fastapi import FastAPI
from app.routers.products import router


app = FastAPI()

app.include_router(router)
