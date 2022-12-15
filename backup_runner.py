from logging import getLogger

from boto3 import client
from boto3_type_annotations.s3 import Client as S3Client
from src.packages.data_backup import reader
from src import settings
import redis.asyncio as redis

import asyncio

logger = getLogger(__name__)
logger.addHandler(settings.handler)


async def run(s3_client: S3Client, redis_client: redis):

    async with redis_client.pubsub() as pubsub:
        str_channels = ",".join(settings.REDIS_CHANNELS)
        await pubsub.subscribe(*settings.REDIS_CHANNELS)

        future = asyncio.create_task(reader(channelPubSub=pubsub, s3_client=s3_client))

        logger.info(f"listen to the channels: {str_channels}")

        await future


if __name__ == "__main__":
    """
    Preparing connections to start training application.
    """

    s3_client: S3Client = client(
        service_name="s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
    )

    redis_client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0,
        password=settings.REDIS_PASS,
    )

    asyncio.run(run(s3_client=s3_client, redis_client=redis_client))
