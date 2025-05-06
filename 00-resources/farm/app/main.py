
from fastapi import FastAPI
from typing import Union
from models.products import Product



app = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/product/{product_id}")
def read_item(product_id: int, q: Union[str, None] = None):
    return {"item_id": product_id, "q": q}


@app.put("/products/{product_id}")
def update_item(product_id: int, product: Product):
    return {"item_id": product_id, "item_name": product.name}