from typing import Union

from fastapi import FastAPI

from main import main

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/nonAttackingQueens/{queensNumber}")
def read_item(queensNumber: int):
    results = main(queensNumber)
    return {"combinaciones": results[0], "numCombinaciones": results[1]}