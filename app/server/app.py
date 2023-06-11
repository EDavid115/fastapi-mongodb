### RGX Project ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from server.auth.jwt_bearer import JWTBearer

from config import settings
from server.database.connect import connectDB
from server.routes.dashboard import router as DashboardRouter
from server.routes.proyects import router as ProyectsRouter
from server.routes.auth import router as AuthRouter
from server.routes.users import router as UsersRouter

app = FastAPI()

token_listener = JWTBearer()

@app.on_event("startup")
def start_database():
    connectDB(settings.MONGODB_URI, settings.MONGODB_DATABASE)
    
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

# Routes
app.include_router(DashboardRouter, prefix="/dashboard", tags=["dashboard"])
app.include_router(ProyectsRouter, prefix="/proyect", tags=["proyects"])
app.include_router(AuthRouter, prefix="/auth", tags=["auth"])
app.include_router(UsersRouter, prefix="/users", tags=["users"], dependencies=[Depends(token_listener)])

@app.get("/", tags=["RGX Root"])
async def root():
	return {
		"message": "Welcome to RGX",
		"Swagger": "http://127.0.0.1:8000/docs",
		"Redocly": "http://127.0.0.1:8000/redoc"
	}
