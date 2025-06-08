from typing import Optional, TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
if TYPE_CHECKING:
    from .Cuestionario import Cuestionario, CuestionarioPublic

class ProfesorBase(SQLModel):
    nombre: str = Field(index=True)
    correo: str = Field(unique=True)

class Profesor(ProfesorBase, table=True):
    id: Optional[int] = Field(primary_key=True, index=True, default=None)
    contrasena: str = Field()
    cuestionarios: list["Cuestionario"] = Relationship(back_populates="profesor")

class ProfesorCreate(ProfesorBase):
    contrasena: str

class ProfesorPublic(ProfesorBase):
    id: int

class ProfesorUpdate(SQLModel):
    nombre: Optional[str] = None
    correo: Optional[str] = None
    contrasena: Optional[str] = None

class ProfesorConCuestionarios(ProfesorPublic):
    cuestionarios: list["CuestionarioPublic"] = []

from .Cuestionario import Cuestionario, CuestionarioPublic
ProfesorConCuestionarios.model_rebuild()
