import enum
import json
from typing import Optional, TYPE_CHECKING
from sqlmodel import Enum, Relationship, SQLModel, Field, Column
if TYPE_CHECKING:
    from .Cuestionario import Cuestionario, CuestionarioPublic
    from .Respuesta import Respuesta, RespuestaPublic

class Tipos(enum.Enum):
    abierta = 1
    opcion_multiple = 2

class PreguntaBase(SQLModel):
    contenido: str
    opciones: str
    tipo: Tipos = Field(sa_column=Column(Enum(Tipos)))
    cuestionario_id: int = Field(index=True, foreign_key="cuestionario.id")

    def get_opciones(self) -> list[str]:
        return json.loads(self.opciones) if self.opciones else []

    def set_opciones(self, opciones: list[str]):
        self.opciones = json.dumps(opciones)

class Pregunta(PreguntaBase, table=True):
    id: Optional[int] = Field(primary_key=True, index=True, default=None)
    respuesta_correcta: str = Field(default="")

    cuestionario: Optional["Cuestionario"] = Relationship(back_populates="preguntas")
    respuesta: list["Respuesta"] = Relationship(back_populates="pregunta")

class PreguntaCreate(PreguntaBase):
    pass

class PreguntaPublic(PreguntaBase):
    id: int

class PreguntaUpdate(SQLModel):
    contenido: Optional[str] = None
    opciones: Optional[str] = None
    respuesta_correcta: Optional[str] = None
    tipo: Optional[Tipos] = None
    cuestionario_id: Optional[int] = None

class PreguntaConCuestionarioYRespuestas(PreguntaPublic):
    cuestionario: Optional["CuestionarioPublic"] = None
    respuestas: list["RespuestaPublic"] = []

from .Cuestionario import Cuestionario, CuestionarioPublic
from .Respuesta import Respuesta, RespuestaPublic
PreguntaConCuestionarioYRespuestas.model_rebuild()
