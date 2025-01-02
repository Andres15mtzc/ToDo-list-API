from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def connect_to_database():
    print("Conexión establecida con la base de datos.")
    # Implementar conexion

async def disconnect_from_database():
    print("Conexión cerrada con la base de datos.")
    # Implementar desconexion

# Crear tablas
Base.metadata.create_all(bind=engine)
