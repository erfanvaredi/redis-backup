import asyncio
import redis.asyncio as redis

import sys
sys.path.insert(0,'..')

from src import settings

STOPWORD = "STOP"

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--m", type=str, default="random_message")
parser.add_argument("--c", type=str, default=settings.REDIS_CHANNELS[0])
opt = parser.parse_args()

message = opt.m
channel = opt.c

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, password=settings.REDIS_PASS)

async def produce():
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("channel:1", "channel:2")

        # future = asyncio.create_task(reader(pubsub))

        await r.publish(channel, f"{message}")

        # await future

# for i in range(2):
asyncio.run(produce())