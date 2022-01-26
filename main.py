from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")  # app.post/put/delete/options/head/patch/trace
async def root():
    return {"message": "Hello, world"}


@app.get('/items/{item_id}')
async def get_item(item_id):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item
