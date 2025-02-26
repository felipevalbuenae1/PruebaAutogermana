from typing import Union
from fastapi import FastAPI, Depends
import asyncpg
from fastapi.exceptions import HTTPException
from database import get_db
from auth import hash_password, verify_password, create_jwt, verify_jwt
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Crear instancia de FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los dominios (puedes especificar uno en particular)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)
# Modelo de datos para la creación de usuario
class UserCreate(BaseModel):
    username: str  # Nombre de usuario
    password: str  # Contraseña del usuario

# Endpoint para registrar un usuario
@app.post("/register")
async def register(user: UserCreate, db=Depends(get_db)):
    hashed_password = hash_password(user.password)  # Encriptar la contraseña
    try:
        await db.execute("INSERT INTO usuarios (username, password) VALUES ($1, $2)", user.username, hashed_password)
        return {"message": "Usuario registrado"}  # Mensaje de éxito
    except Exception:
        raise HTTPException(status_code=400, detail="Usuario ya existe")  # Manejo de error si el usuario ya existe

# Endpoint para inicio de sesión
@app.post("/login")
async def login(user: UserCreate, db=Depends(get_db)):
    db_user = await db.fetchrow("SELECT * FROM usuarios WHERE username = $1", user.username)  # Buscar usuario en la BD
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")  # Error si las credenciales son incorrectas

    token = create_jwt({"sub": db_user["username"]})  # Generar token JWT
    return {"access_token": token, "token_type": "bearer"}  # Devolver token JWT

# Endpoint protegido con autenticación JWT
@app.get("/protected")
async def protected_route(user=Depends(verify_jwt)):
    return {"message": f"Hola, {user['sub']}, tienes acceso autorizado"}  # Mensaje de bienvenida si el token es válido

# Endpoint para obtener todos los vehículos (requiere autenticación)
@app.get("/vehiculos")
async def get_vehiculos(db=Depends(get_db), user=Depends(verify_jwt)):
    return await db.fetch("SELECT * FROM vehiculos")  # Consultar todos los vehículos en la BD

# Endpoint para agregar un vehículo (requiere autenticación)
@app.post("/vehiculos")
async def create_vehiculo(marca: str, modelo: str, anio: int, precio: float, db=Depends(get_db), user=Depends(verify_jwt)):
    await db.execute("INSERT INTO vehiculos (marca, modelo, anio, precio) VALUES ($1, $2, $3, $4)", marca, modelo, anio, precio)
    return {"message": "Vehículo agregado"}  # Mensaje de éxito

# Endpoint para borrar un vehículo por ID
@app.delete("/vehiculos/{id}")
async def delete_vehiculo(id: int, db=Depends(get_db)):
    await db.execute("DELETE FROM vehiculos WHERE id = $1", id)  # Eliminar vehículo con ID específico
    return {"message": "Vehículo eliminado"}  # Mensaje de éxito
