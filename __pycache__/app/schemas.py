from pydantic import BaseModel
from typing import Union, List, Dict

class ParameterBase(BaseModel):
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