import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def startup():
    return {"message" : "Server is up!"}

@app.get("/greet")
def greet():
    return {"message" : "Server says Hello!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")