from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/imie/{plec}")
def read_item(plec: str):
    return {"imie": plec}