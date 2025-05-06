from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductReponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_product,
    get_products,
    delete_product,
    update_product
)

router = APIRouter()

### criar minha rota de buscar 1 item

### criar minha rota de buscar todos os itens

### criar minha rota de add 1 item

### criar minha rota de deletar um item

### criar minha rota de fazer um update nos itens   