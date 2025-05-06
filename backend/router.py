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
@router.get("/products/{produto}", response_model=ProductReponse)
def read_one_peroduct(product_id:int, db:Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException (status_code=404, detail= "o id do produto não existe")
    return db_product

### criar minha rota de add 1 item
@router.post("/products/{produto}", response_model=ProductReponse)
def create_product_route(product: ProductCreate, db:Session = Depends(get_db)):
    return create_product(product=product,db=db)

### criar minha rota de deletar um item
@router.delete("/products/{produto}}", response_model=ProductReponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(product_id=product_id, db=db)
    if db_product is None:
        raise HTTPException(status_code=404, detail="o id do produto não existe")
    return delete_product(db_product=db_product, db=db)


### criar minha rota de fazer um update nos itens
@router.patch("/products/{produto}}", response_model=ProductReponse)
def att_product(product_id: int, product: ProductUpdate,db: Session = Depends(get_db)):
    db_product = update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="o id do produto não existe")
    return delete_product(db_product=db_product, product_id=product_id, db=db)