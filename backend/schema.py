from pydantic import BaseModel, PositiveFloat, EmailStr, validate_call
from enum import Enum
from datetime import datetime
from typing import Optional

# A função do schema é validar como os dados vão trafegar, ou seja que o usuário estão inserindo/atualizando, por isso usamos o pydantic

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreat(ProductBase):
    pass

# O único que vai conversar com meu models, pois é para fazermos um select no banco, então queremos ver todos os dados, diferente do usuário que não precisa criar id nem a data de criação do produto
class ProductReponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes: True

class             