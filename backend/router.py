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

### criar minha rota de buscar todos os itens
### sempre vamos ter 2 atributos obrigatórios, o PATH (endereço da minha api)e o RESPONSE)
@router.get("/products/", response_model=List[ProductReponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

### criar minha rota de buscar 1 item
@router.get()

### criar minha rota de add 1 item
@router.post()

### criar minha rota de deletar um item
@router.delete()

### criar minha rota de fazer um update nos itens
@router.update()