from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, crud
from app.database import SessionLocal, engine, Base
from typing import Union, List, Dict

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic modelo para las solicitudes/respuestas
class ParameterBase(Base):
    name: str
    value: Union[None, bool, int, str, List[Union[str, int, bool]], Dict[str, Union[str, int, bool]]]

class ParameterCreate(ParameterBase):
    pass

class ParameterUpdate(ParameterBase):
    pass

class Parameter(ParameterBase):
    id: int

    class Config:
        orm_mode = True

@app.post("/parameters/", response_model=Parameter)
async def create_parameter(parameter: Parameter, db: Session = Depends(get_db)):
    db_parameter = crud.get_parameter(db, parameter.name)
    if db_parameter:
        raise HTTPException(status_code=400, detail="Parameter existente")
    return crud.create_parameter(db=db, parameter=parameter)

@app.get("/parameters/{name}", response_model=Parameter)
async def read_parameter(name: str, db: Session = Depends(get_db)):
    db_parameter = crud.get_parameter(db, name)
    if db_parameter is None:
        raise HTTPException(status_code=404, detail="Parametro not found")
    return db_parameter

@app.put("/parameters/{name}", response_model=Parameter)
async def update_parameter(name: str, parameter: Parameter, db: Session = Depends(get_db)):
    db_parameter = crud.get_parameter(db, name)
    if db_parameter is None:
        raise HTTPException(status_code=404, detail="Parametro not found")
    return crud.update_parameter(db=db, name=name, value=parameter.value)