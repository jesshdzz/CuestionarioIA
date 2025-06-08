from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from database import get_session
from models.Pregunta import Pregunta, PreguntaConCuestionarioYRespuestas, PreguntaCreate, PreguntaPublic, PreguntaUpdate

router = APIRouter(prefix="/preguntas")

# Endpoint para agregar una pregunta
@router.post("/", response_model=PreguntaCreate)
async def create_pregunta(pregunta: PreguntaCreate, session: AsyncSession = Depends(get_session)):
    db_pregunta = Pregunta.model_validate(pregunta)
    session.add(db_pregunta)
    await session.commit()
    await session.refresh(db_pregunta)
    return db_pregunta

# Endpoint para obtener todas las preguntas
@router.get("/", response_model=list[PreguntaPublic])
async def read_preguntas(skip: int = 0, limit: int = Query(default=10, le=20), session: AsyncSession = Depends(get_session)):
    preguntas = await session.exec(select(Pregunta).offset(skip).limit(limit))
    return preguntas.all()

# Endpoint para obtener una pregunta por import PreguntaID
@router.get("/{pregunta_id}", response_model=PreguntaConCuestionarioYRespuestas)
async def read_pregunta(pregunta_id: int, session: AsyncSession = Depends(get_session)):
    pregunta = await session.get(Pregunta, pregunta_id, options=[selectinload(Pregunta.cuestionario), selectinload(Pregunta.respuesta)])
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta not found")
    return pregunta

# Endpoint para actualizar una pregunta
@router.patch("/{pregunta_id}", response_model=PreguntaPublic)
async def update_pregunta(pregunta_id: int, pregunta: PreguntaUpdate, session: AsyncSession = Depends(get_session)):
    pregunta_db = await session.get(Pregunta, pregunta_id)
    if not pregunta_db:
        raise HTTPException(status_code=404, detail="Pregunta not found")
    pregunta_data = pregunta.model_dump(exclude_unset=True)
    for key, value in pregunta_data.items():
        setattr(pregunta_db, key, value)
    session.add(pregunta_db)
    await session.commit()
    await session.refresh(pregunta_db)
    return pregunta_db

# Endpoint para eliminar una pregunta
@router.delete("/{pregunta_id}")
async def delete_pregunta(pregunta_id: int, session: AsyncSession = Depends(get_session)):
    pregunta = await session.get(Pregunta, pregunta_id)
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta not found")
    await session.delete(pregunta)
    await session.commit()
    return  {'ok': True}
