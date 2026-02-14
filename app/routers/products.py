from fastapi import APIRouter, Path, Query
from fastapi.exceptions import HTTPException
from fastapi import status
from typing import Annotated

from app.db.database import Localsession
from app.models.products import Product

router = APIRouter(
    prefix="/products",
    tags=["Product Endpoints"]
)

    
# @router.get("")
# def price_query( 
#             min_price: Annotated[float| None,Query(gt=0) ] = None, 
#             max_price: Annotated[float| None, Query(gt=0)] = None
#         ):
    
#     db=Localsession()
    
#     query = db.query(Product)  # Select * from Product  -> Hamma produclarni qaytaradi  
    
#     print(min_price,max_price)
    
#     if min_price is not None:    
#         query = query.filter(Product.price >= min_price)   # WHERE min_price >= 100
        
        
#     if max_price is not None:
#         query = query.filter(Product.price <= max_price)  #WHERE max_price <= 200
#         print(max_price)
        
#     result = []
    
#     products = query.all()   # all()  Birlashtiradi  min_price AND max_price:
    
#     for product in products:
#         result.append({
#             "id": product.id,
#             "name":product.name,
#             "price":product.price
            
#         })
    
#     return result


@router.get("")
def get_page(
    page: Annotated[int,Query(ge=1)]=1,
    limit: Annotated[int,Query(ge=10,le=100)]=10
):
    
    db = Localsession()
    
    offset = (page-1) * limit
    
    products = db.query(Product).offset(offset).limit(limit).all()
    
    result = []
    
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "price": product.price
        })
    return result

feed_query = Query(min_length=5, max_length=30,description="Production name search")

@router.get("/search")
def get_name(search: Annotated[str, feed_query]="all"):     
    
    db = Localsession()
    
    names = db.query(Product).filter(Product.name.ilike(f"%{search}%")).all()     # Search Datadan Malumotlarni qidiriss
    
    result = []
    
    
    for name in names:
        
        result.append({
            "id": name.id,
            "name": name.name     
        })


               
    return result   
        


@router.get("/{product_id}")
def get_one_product(product_id: Annotated[int,Path(gt=0)]):
    db = Localsession()
    
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bunday username yuq")
    
    return product
    
    



