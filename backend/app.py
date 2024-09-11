from fastapi import FastAPI
from backend.api.api import router as api_products
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://127.0.0.1:8081",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_products)

