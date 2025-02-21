from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class InputPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
    
@app.post("/echo")
async def echo(payload: InputPayload):
    return payload

@app.get("/status")
async def status():
    return {"message": "API is running", "model_loaded": model is not None}

