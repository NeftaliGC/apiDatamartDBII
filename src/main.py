from fastapi import FastAPI
from src.functions import Functions

app = FastAPI()

@app.get("/")
def read_root():
    fun = Functions()
    print(fun)
    return fun.connect()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
