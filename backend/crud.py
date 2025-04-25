from sqlalchemy.orm import Session
from schemas import ProductBase, ProductCreate
from models import ProductModel

# get all (select * from)

def get_products(db: Session):
    "Função onde retorna todos os produtos"
    return db.query(ProductModel).all()

# get where id = 1
def get_product(db: Session, product_id: int):
    "Função onde retorna somente um produto, usando where"
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# insert into (creat)

# update where id = 1

# delete where id = 1
