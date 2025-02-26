from pydantic import BaseModel
from datetime import datetime

# Modelo de Vehículo
class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    anio: int
    precio: float

class VehiculoCreate(VehiculoBase):
    pass

class Vehiculo(VehiculoBase):
    id: int

    class Config:
        from_attributes = True

# Modelo de Cliente
class ClienteBase(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        from_attributes = True

# Modelo de Concesionario
class ConcesionarioBase(BaseModel):
    nombre: str
    direccion: str
    ciudad: str

class ConcesionarioCreate(ConcesionarioBase):
    pass

class Concesionario(ConcesionarioBase):
    id: int

    class Config:
        from_attributes = True

# Modelo de Transacción
class TransaccionBase(BaseModel):
    vehiculo_id: int
    cliente_id: int
    concesionario_id: int
    fecha_venta: datetime
    precio_venta: float

class TransaccionCreate(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int

    class Config:
        from_attributes = True
