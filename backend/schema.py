from pydantic import BaseModel, PositiveFloat, EmailStr, validate_call
from enum import Enum
from datetime import datetime
from typing import Optional

# A função do schema é validar como os dados vão trafegar, por isso usamos o pydantic

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreat(ProductBase):
    pass

