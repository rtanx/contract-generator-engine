from fastapi import FastAPI
from .routers import routes

app = FastAPI(debug=True)

app.include_router(routes.router)
