from typing import Union

from fastapi import FastAPI

from main import main

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}




@app.get("/nonAttackingQueens/{queensNumber}")
def read_item(queensNumber: int):
    if queensNumber>0:
        results = main(queensNumber)
        return {"combinaciones": results[0], "numCombinaciones": results[1]}
    else:
        return {"error": "Se debe ingresar un número mayor a 0"}