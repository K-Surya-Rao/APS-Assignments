<<<<<<< HEAD
from fastapi import FastAPI
from routers import products

app = FastAPI()

app.include_router(products.router)
=======
from fastapi import FastAPI
from routers import products

app = FastAPI()

app.include_router(products.router)
>>>>>>> bac09dc2cd1f73c40978572117a40b1d6d68528a
