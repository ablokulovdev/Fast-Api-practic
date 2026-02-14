from datetime import datetime
from typing import List
from pydantic import BaseModel


class ProductResponse(BaseModel):          # Objectni Dictionaryga ugirib Response qaytaradi Frontendga 
    
    id: int
    name: str
    description: str
    category: str
    brand : str
    price : float
    currency: str
    quantity_in_stock: int
    is_active: bool
    discount_percent: int | None=None
    rating: float
    
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True      # Product model dictonatyga o'girish ruxsat berib quyishim kerak.
        
        
class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int
    limit: int
    page:  int
    page: int
    class Config:
        from_attributes = True
        
class ProductSearchListResponses(BaseModel):
    products: List[ProductResponse]
    
    class Config:
        from_attributes = True