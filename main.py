import asyncio
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/wait")
async def wait_api(request: Request):
    kwargs = await request.json()
    await asyncio.sleep(110)
    
    return {"data": kwargs}
