from fastapi import FastAPI

app_instance = FastAPI()

@app_instance.get("/")
def root_endpoint():
    return {"message": "docker + fastapi working"}