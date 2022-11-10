from fastapi import FastAPI
from .routers import routes
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(debug=True)

app.include_router(routes.router)
