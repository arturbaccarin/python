from email.policy import default
from typing import Optional

from sqlmodel import Field, SQLModel

# table -> True vai ser schema e table
# com false vai ser somente schema
class CursoModel(SQLModel, table=True):
    __tablename__: str = 'cursos'

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int