from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import redis.asyncio as redis

from src import settings

app = FastAPI()
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, password=settings.REDIS_PASS)

@app.get("/")
def welcome():
    return {'hello':'world'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/send/{channel}/{key}")
async def read_item(channel: str,key: str, q: Union[str, None] = None):
    async with redis_client.pubsub() as pubsub:
        
        await pubsub.subscribe(channel)

        await redis_client.publish(key)

