### RGX Project ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from server.routes.dashboard import router as DashboardRouter

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dashboard
app.include_router(DashboardRouter, prefix="/dashboard", tags=["dashboard"])


@app.get("/", tags=["RGX Root"])
async def root():
	return {
		"message": "Welcome to RGX",
		"Swagger": "http://127.0.0.1:8000/docs",
		"Redocly": "http://127.0.0.1:8000/redoc"
	}
