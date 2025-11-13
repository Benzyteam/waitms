import asyncio
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/wait")
async def wait_api(request: Request):
    kwargs = await request.json()
    await asyncio.sleep(40)
    
    return {"data": kwargs}

@app.post("/wait/30")
async def wait_api(request: Request):
    kwargs = await request.json()
    await asyncio.sleep(30)
    
    return {"data": kwargs}
