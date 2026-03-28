from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID

class TimeBase(BaseModel):

    # Esses ... (três pontos) dentro do Field() no Pydantic significam que o campo é obrigatório.
    # No Python isso é o objeto especial chamado Ellipsis. O Pydantic usa ele como sinal de: “este valor precisa ser fornecido”. 

    name: str = Field(..., min_length=2, max_length=100, example="São Paulo FC")

    @field_validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('O nome não pode ser apenas espaços em branco.')
        return v.title()