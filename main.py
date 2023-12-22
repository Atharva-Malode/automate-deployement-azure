from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World}"}

@app.get("/Bored")
def bored():
    response = requests.get("https://www.boredapi.com/api/activity")
    return response.json()