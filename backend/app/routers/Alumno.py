from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from database import get_session
import models.Alumno as Alumno

router = APIRouter(prefix="/alumnos")

# Endpoint para agregar un alumno
@router.post("/", response_model=Alumno.AlumnoCreate)
async def create_alumno(alumno: Alumno.AlumnoCreate, session: AsyncSession = Depends(get_session)):
    db_alumno = Alumno.Alumno.model_validate(alumno)
    session.add(db_alumno)
    await session.commit()
    await session.refresh(db_alumno)
    return db_alumno

# Endpoint para obtener todos los alumnos
@router.get("/", response_model=list[Alumno.AlumnoPublic])
async def read_alumnos(skip: int = 0, limit: int = Query(default=10, le=20), session: AsyncSession = Depends(get_session)):
    alumnos = await session.exec(select(Alumno).offset(skip).limit(limit))
    return alumnos.all()

# Endpoint para obtener un alumno por import AlumnoID
@router.get("/{alumno_id}", response_model=Alumno.AlumnoPublic)
async def read_alumno(alumno_id: int, session: AsyncSession = Depends(get_session)):
    alumno = await session.get(Alumno, alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno not found")
    return alumno

# Endpoint para actualizar un alumno
@router.patch("/{alumno_id}", response_model=Alumno.AlumnoPublic)
async def update_alumno(alumno_id: int, alumno: Alumno.AlumnoUpdate, session: AsyncSession = Depends(get_session)):
    alumno_db = await session.get(Alumno, alumno_id)
    if not alumno_db:
        raise HTTPException(status_code=404, detail="Alumno not found")
    alumno_data = alumno.model_dump(exclude_unset=True)
    for key, value in alumno_data.items():
        setattr(alumno_db, key, value)
    session.add(alumno_db)
    await session.commit()
    await session.refresh(alumno_db)
    return alumno_db

# Endpoint para eliminar un alumno
@router.delete("/{alumno_id}")
async def delete_alumno(alumno_id: int, session: AsyncSession = Depends(get_session)):
    alumno = await session.get(Alumno, alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno not found")
    await session.delete(alumno)
    await session.commit()
    return  {'ok': True}
