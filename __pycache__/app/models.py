from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Parameter(Base):
    __tablename__ = "parameters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    value = Column(JSON)