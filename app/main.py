from fastapi import FastAPI

app = FastAPI(title="LinkVault", version="0.1.0")

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def read_health():
    return {"status": "healthy"}

@app.get("/about")
async def read_about():
    return {"name": "Ganiyat Olaiwon", "reason": "Learning FastAPI to build production APIs"}