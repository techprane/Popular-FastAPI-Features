from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    """
    Creates a new item in the system.

    Parameters:
    item (Item): An instance of the Item class containing the name and price of the item.

    Returns:
    dict: A dictionary containing the name and price of the created item.
    """
    return {"name": item.name, "price": item.price}



def get_token(token: str):
    return token

@app.get("/secure/", dependencies=[Depends(get_token)])
def secure_route():
    return {"message": "Secure Access"}

@app.get("/async_items/")
async def read_async_item():
    return {"message": "This is asynchronous"}






