from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from database import get_session
from models.Respuesta import Respuesta, RespuestaConPreguntaYAlumno, RespuestaCreate, RespuestaPublic, RespuestaUpdate

router = APIRouter(prefix="/respuestas")

# Endpoint para agregar una respuesta
@router.post("/", response_model=RespuestaCreate)
async def create_respuesta(respuesta: RespuestaCreate, session: AsyncSession = Depends(get_session)):
    db_respuesta = Respuesta.model_validate(respuesta)
    session.add(db_respuesta)
    await session.commit()
    await session.refresh(db_respuesta)
    return db_respuesta

# Endpoint para obtener todas las respuestas
@router.get("/", response_model=list[RespuestaPublic])
async def read_respuestas(skip: int = 0, limit: int = Query(default=10, le=20), session: AsyncSession = Depends(get_session)):
    respuestas = await session.exec(select(Respuesta).offset(skip).limit(limit))
    return respuestas.all()

# Endpoint para obtener una respuesta por import RespuestaID
@router.get("/{respuesta_id}", response_model=RespuestaConPreguntaYAlumno)
async def read_respuesta(respuesta_id: int, session: AsyncSession = Depends(get_session)):
    respuesta = await session.get(Respuesta, respuesta_id, options=[selectinload(Respuesta.pregunta), selectinload(Respuesta.alumno)])
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta not found")
    return respuesta

# Endpoint para actualizar una respuesta
@router.patch("/{respuesta_id}", response_model=RespuestaPublic)
async def update_respuesta(respuesta_id: int, respuesta: RespuestaUpdate, session: AsyncSession = Depends(get_session)):
    respuesta_db = await session.get(Respuesta, respuesta_id)
    if not respuesta_db:
        raise HTTPException(status_code=404, detail="Respuesta not found")
    respuesta_data = respuesta.model_dump(exclude_unset=True)
    for key, value in respuesta_data.items():
        setattr(respuesta_db, key, value)
    session.add(respuesta_db)
    await session.commit()
    await session.refresh(respuesta_db)
    return respuesta_db

# Endpoint para eliminar una respuesta
@router.delete("/{respuesta_id}")
async def delete_respuesta(respuesta_id: int, session: AsyncSession = Depends(get_session)):
    respuesta = await session.get(Respuesta, respuesta_id)
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta not found")
    await session.delete(respuesta)
    await session.commit()
    return  {'ok': True}
