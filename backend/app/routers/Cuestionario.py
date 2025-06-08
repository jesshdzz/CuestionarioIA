from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from database import get_session
from models.Cuestionario import Cuestionario, CuestionarioConProfesorYPreguntas, CuestionarioCreate, CuestionarioPublic, CuestionarioUpdate

router = APIRouter(prefix="/cuestionarios")

# Endpoint para agregar un cuestionario
@router.post("/", response_model=CuestionarioCreate)
async def create_cuestionario(*, cuestionario: CuestionarioCreate, session: AsyncSession = Depends(get_session)):
    db_cuestionario = Cuestionario.model_validate(cuestionario)
    session.add(db_cuestionario)
    await session.commit()
    await session.refresh(db_cuestionario)
    return db_cuestionario

# Endpoint para obtener todos los cuestionarios
@router.get("/", response_model=list[CuestionarioPublic])
async def read_cuestionarios(*, skip: int = 0, limit: int = Query(default=10, le=20), session: AsyncSession = Depends(get_session)):
    cuestionarios = await session.exec(select(Cuestionario).offset(skip).limit(limit))
    return cuestionarios.all()

# Endpoint para obtener un cuestionario por import CuestionarioID
@router.get("/{cuestionario_id}", response_model=CuestionarioConProfesorYPreguntas)
async def read_cuestionario(*, cuestionario_id: int, session: AsyncSession = Depends(get_session)):
    cuestionario = await session.get(Cuestionario, cuestionario_id, options=[selectinload(Cuestionario.profesor)])
    if not cuestionario:
        raise HTTPException(status_code=404, detail="Cuestionario not found")
    return cuestionario

# Endpoint para actualizar un cuestionario
@router.patch("/{cuestionario_id}", response_model=CuestionarioPublic)
async def update_cuestionario(*, cuestionario_id: int, cuestionario: CuestionarioUpdate, session: AsyncSession = Depends(get_session)):
    cuestionario_db = await session.get(Cuestionario, cuestionario_id)
    if not cuestionario_db:
        raise HTTPException(status_code=404, detail="Cuestionario not found")
    cuestionario_data = cuestionario.model_dump(exclude_unset=True)
    for key, value in cuestionario_data.items():
        setattr(cuestionario_db, key, value)
    session.add(cuestionario_db)
    await session.commit()
    await session.refresh(cuestionario_db)
    return cuestionario_db

# Endpoint para eliminar un cuestionario
@router.delete("/{cuestionario_id}")
async def delete_cuestionario(*, cuestionario_id: int, session: AsyncSession = Depends(get_session)):
    cuestionario = await session.get(Cuestionario, cuestionario_id)
    if not cuestionario:
        raise HTTPException(status_code=404, detail="Cuestionario not found")
    await session.delete(cuestionario)
    await session.commit()
    return  {'ok': True}
