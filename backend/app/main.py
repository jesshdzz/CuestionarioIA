from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database import init_db
from routers import Alumno, Profesor, Cuestionario, Pregunta

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crear la base de datos y las tablas al iniciar la aplicación
    await init_db()
    print("Aplicacion iniciada.")
    yield
    print("Aplicacion terminada.")

app = FastAPI(
    title="API de Alumnos",
    description="API para gestionar alumnos en un sistema educativo",
    version="1.0.0",
    lifespan=lifespan
 )

# Configuración de CORS para permitir solicitudes desde un dominio específico
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3050"],  # Cambia esto según tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


app.include_router(Alumno.router, tags=["alumnos"])
app.include_router(Profesor.router, tags=["profesores"])
app.include_router(Cuestionario.router, tags=["cuestionarios"])
app.include_router(Pregunta.router, tags=["preguntas"])