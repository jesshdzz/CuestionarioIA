from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡FastAPI está funcionando desde Docker!"}
