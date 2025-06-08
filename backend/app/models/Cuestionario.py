from typing import Optional, TYPE_CHECKING
import datetime
from sqlmodel import Relationship, SQLModel, Field
if TYPE_CHECKING:
    from .Profesor import Profesor, ProfesorPublic
    from .Pregunta import Pregunta, PreguntaPublic

class CuestionarioBase(SQLModel):
    titulo: str = Field(index=True)
    fecha_creacion: datetime.datetime = Field(default_factory=datetime.datetime.now)

    profesor_id: int = Field(index=True, foreign_key="profesor.id")

class Cuestionario(CuestionarioBase, table=True):
    id: Optional[int] = Field(primary_key=True, index=True, default=None)
    profesor: Optional["Profesor"] = Relationship(back_populates="cuestionarios")
    preguntas: list["Pregunta"] = Relationship(back_populates="cuestionario")

class CuestionarioCreate(CuestionarioBase):
    pass

class CuestionarioPublic(CuestionarioBase):
    id: int

class CuestionarioUpdate(SQLModel):
    titulo: Optional[str] = None
    profesor_id: Optional[int] = None
    fecha_creacion: Optional[datetime.datetime] = None

class CuestionarioConProfesorYPreguntas(CuestionarioPublic):
    profesor: Optional["ProfesorPublic"] = None
    Preguntas: list["PreguntaPublic"] = []

from .Profesor import Profesor, ProfesorPublic
from .Pregunta import Pregunta, PreguntaPublic
CuestionarioConProfesorYPreguntas.model_rebuild()