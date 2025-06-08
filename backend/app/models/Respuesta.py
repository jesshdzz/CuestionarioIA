from typing import Optional, TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
if TYPE_CHECKING:
    from .Pregunta import Pregunta, PreguntaPublic
    from .Alumno import Alumno, AlumnoPublic

class RespuestaBase(SQLModel):
    pregunta_id: int = Field(index=True, foreign_key="pregunta.id")
    alumno_id: int = Field(index=True, foreign_key="alumno.id")
    respuesta: str
    calificacion: Optional[float] = None

class Respuesta(RespuestaBase, table=True):
    id: Optional[int] = Field(primary_key=True, index=True, default=None)
    pregunta: Optional["Pregunta"] = Relationship(back_populates="respuesta")
    alumno: Optional["Alumno"] = Relationship(back_populates="respuestas")

class RespuestaCreate(RespuestaBase):
    pass

class RespuestaPublic(RespuestaBase):
    id: int

class RespuestaUpdate(SQLModel):
    pregunta_id: Optional[int] = None
    usuario_id: Optional[int] = None
    respuesta: Optional[str] = None
    calificacion: Optional[float] = None

class RespuestaConPreguntaYAlumno(RespuestaPublic):
    pregunta: Optional["PreguntaPublic"] = None
    usuario: Optional["AlumnoPublic"] = None

from .Pregunta import Pregunta, PreguntaPublic
from .Alumno import Alumno, AlumnoPublic
RespuestaConPreguntaYAlumno.model_rebuild()
