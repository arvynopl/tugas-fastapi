from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Deployment by Arvyno Pranata Limahardja (NIM: 18222007)"}