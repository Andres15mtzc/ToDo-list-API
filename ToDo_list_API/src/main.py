from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import connect_to_database, disconnect_from_database
from app.routes import auth, tasks

# Aqui se simula la conexion a la database en caso de tener una base de datos externa
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que se ejecuta cuando la aplicación inicia
    print("Conectando a la base de datos...")
    await connect_to_database()
    yield
    # Código que se ejecuta cuando la aplicación se cierra
    print("Desconectando de la base de datos...")
    await disconnect_from_database()

# Instancia de la aplicación FastAPI con el ciclo de vida definido
app = FastAPI(lifespan=lifespan)

# Registro de rutas de autorizacion y tareas
app.include_router(auth.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "API To-Do List funcionando correctamente"}
