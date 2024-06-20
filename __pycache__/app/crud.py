from sqlalchemy.orm import Session
from app.models import Parameter
from app.schemas import ParameterCreate, ParameterUpdate


def get_parameter(db: Session, name: str):
    return db.query(Parameter).filter(Parameter.name == name).first()

def create_parameter(db: Session, parameter: Parameter):
    db.add(parameter)
    db.commit()
    db.refresh(parameter)
    return parameter

def update_parameter(db: Session, name: str, value: dict):
    parameter = get_parameter(db, name)
    parameter.value = value
    db.commit()
    db.refresh(parameter)
    return parameter