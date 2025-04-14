from pydantic import BaseModel, Optional
from typing import Union
class Product(BaseModel):
    name:str
    price: float
    quantity: int
    is_offer: Union[bool, None] = None
    description: Optional[str]= None
