from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def inicial():
    return{"message":"Hello World"}