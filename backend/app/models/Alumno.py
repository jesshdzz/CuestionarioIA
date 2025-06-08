from typing import Optional
from sqlmodel import SQLModel, Field

class AlumnoBase(SQLModel):
    nombre: str = Field(index=True)
    correo: str = Field(unique=True)
    grupo: str
    grado: int

class Alumno(AlumnoBase, table=True):
    id: Optional[int] = Field(primary_key=True, index=True, default=None)
    contrasena: str = Field()

    class Config:
        table_name = "alumnos"

class AlumnoCreate(AlumnoBase):
    contrasena: str

class AlumnoPublic(AlumnoBase):
    id: int

class AlumnoUpdate(SQLModel):
    nombre: Optional[str] = None
    correo: Optional[str] = None
    contrasena: Optional[str] = None
    grupo: Optional[str] = None
    grado: Optional[int] = None
