from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int

class Exc_item(BaseModel):
    path: str
    query:str
    body: str

class Value(BaseModel):
    value: int
    msg : str

app = FastAPI()

@app.get("/")
async def say_hello():
    return {'greetings':'say hello'}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
async def get_item(item_id: int, count: int = 1 ):
    return {"fetch": f"Fetched {count} of {item_id}"}

@app.post("/excercise/")
async def exercise_function(item: Exc_item):
  return item

@app.post("/{path}")
async def path_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body, "multiply": path * query}
