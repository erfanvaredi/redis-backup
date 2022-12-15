import asyncio
import redis.asyncio as redis
from src.packages.utils import save_pickle_to_s3
from datetime import datetime
from boto3 import client
from boto3_type_annotations.s3 import Client as S3Client
import sys
sys.path.insert(0,'..')

from src import settings
from logging import getLogger

logger = getLogger(__name__)
logger.addHandler(settings.handler)


async def reader(channelPubSub: redis.client.PubSub, s3_client: S3Client):
    while True:
        message = await channelPubSub.get_message(ignore_subscribe_messages=True)
        if message is not None:

            message['datetime'] = datetime.utcnow().isoformat()
            message['timestamp'] = datetime.utcnow().timestamp()
            message['decoded_message'] = message['data'].decode()

            if settings.DEBUG is False:
                save_pickle_to_s3(
                    s3_client=s3_client,
                    bucket_name=settings.AWS_BUCKET_NAME,
                    key=message['channel'].decode() + '_' + message['timestamp'] + '_' +'.pickle',
                    obj=message,
                )
            
            logger.info(f"message: {message} has been cloned to s3")


            if message["decoded_message"] == settings.REDIS_STOPWORD:
                break
