from sqlalchemy import desc
from fastapi import APIRouter, Path, Query
from fastapi.exceptions import HTTPException
from fastapi import status
from typing import Annotated, Literal

from app.schemas.product import ProductResponse,ProductListResponse
from app.db.database import Localsession
from app.models.products import Product

router = APIRouter(
    prefix="/products",
    tags=["Product Endpoints"]
)

@router.get("",response_model=list[ProductResponse])
def get_product():
    
    db = Localsession()
    
    products = db.query(Product).all()
    
    return products


@router.get("/page",response_model=ProductListResponse)
def get_page(
    page: Annotated[int,Query(ge=1)]=1,
    limit: Annotated[int,Query(ge=10,le=100)]=10,
    order_by: Literal['created_at','updated_at'] = "updated_at",
    order_sort: Literal['asc','desc'] = 'desc'
):
    
    db = Localsession()
    
    offset = (page-1) * limit
    
    if order_by == "updated_at":
        if order_sort == "desc":
            products = db.query(Product).order_by(desc(Product.updated_at)).offset(offset).limit(limit).all()
            
        else:
            products = db.query(Product).order_by(Product.updated_at).offset(offset).limit(limit).all()

    else:
        if order_sort == "created_at":
            products = db.query(Product).order_by(desc(Product.created_at)).offset(offset).limit(limit).all()
            
        else:
            products = db.query(Product).order_by(Product.created_at).offset(offset).limit(limit).all()
            
    
    products = db.query(Product).offset(offset).limit(limit).all()
    total = db.query(Product).count()
    
    print(total)
    pages = total // limit 
    
    return ProductListResponse(products=products,total=total,limit=limit,page=pages)


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
    
    



