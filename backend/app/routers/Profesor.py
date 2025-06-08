from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from database import get_session
from models.Profesor import Profesor, ProfesorCreate, ProfesorPublic, ProfesorUpdate, ProfesorConCuestionarios


router = APIRouter(prefix="/profesores")

# Endpoint para agregar un profesor
@router.post("/", response_model=ProfesorCreate)
async def create_profesor(*, profesor: ProfesorCreate, session: AsyncSession = Depends(get_session)):
    db_profesor = Profesor.model_validate(profesor)
    session.add(db_profesor)
    await session.commit()
    await session.refresh(db_profesor)
    return db_profesor

# Endpoint para obtener todos los profesors
@router.get("/", response_model=list[ProfesorPublic])
async def read_profesores(*, skip: int = 0, limit: int = Query(default=10, le=20), session: AsyncSession = Depends(get_session)):
    profesores = await session.exec(select(Profesor).offset(skip).limit(limit))
    return profesores.all()

# Endpoint para obtener un profesor por import ProfesorID
@router.get("/{profesor_id}", response_model=ProfesorConCuestionarios)
async def read_profesor(*, profesor_id: int, session: AsyncSession = Depends(get_session)):
    profesor = await session.get(Profesor, profesor_id, options=[selectinload(Profesor.cuestionarios)])
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor

# Endpoint para actualizar un profesor
@router.patch("/{profesor_id}", response_model=ProfesorPublic)
async def update_profesor(*, profesor_id: int, profesor: ProfesorUpdate, session: AsyncSession = Depends(get_session)):
    profesor_db = await session.get(Profesor, profesor_id)
    if not profesor_db:
        raise HTTPException(status_code=404, detail="Profesor not found")
    profesor_data = profesor.model_dump(exclude_unset=True)
    for key, value in profesor_data.items():
        setattr(profesor_db, key, value)
    session.add(profesor_db)
    await session.commit()
    await session.refresh(profesor_db)
    return profesor_db

# Endpoint para eliminar un profesor
@router.delete("/{profesor_id}")
async def delete_profesor(*, profesor_id: int, session: AsyncSession = Depends(get_session)):
    profesor = await session.get(Profesor, profesor_id)
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor not found")
    await session.delete(profesor)
    await session.commit()
    return  {'ok': True}
