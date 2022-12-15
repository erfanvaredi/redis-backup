import asyncio
import redis.asyncio as redis
from datetime import datetime
import sys
sys.path.insert(0,'..')

from src import settings

STOPWORD = "STOP"


async def reader(channel: redis.client.PubSub):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            message['datetime'] = datetime.utcnow().isoformat()
            message['timestamp'] = datetime.utcnow().timestamp()

            decoded_messeg=message['data'].decode()
            
            print(f"----\n(Reader-all) Message Received: {message}")
            print(f"(Reader) Message Received: {decoded_messeg}")
            if message["data"].decode() == STOPWORD:
                print("(Reader) STOP")
                break

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, password=settings.REDIS_PASS)

async def produce():
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("channel:1", "channel:2")

        future = asyncio.create_task(reader(pubsub))

        await r.publish("channel:1", "۱۲۲۲۲۲۲")
        await r.publish("channel:2", "World")
        # await r.publish("channel:1", STOPWORD)

        await future

# for i in range(2):
asyncio.run(produce())