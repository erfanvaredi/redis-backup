import logging
import pickle
import sys
from datetime import datetime

from boto3_type_annotations.s3 import Client
from pydantic import BaseModel, StrictFloat

from src import settings

logger = logging.getLogger(__name__)
logger.addHandler(settings.handler)


def save_to_s3(s3_client: Client, bucket_name: str, key: str, obj):
    """Save an object in S3
    Args:
        s3_client (Client): client connection to Amazon S3
        bucket_name (str): bucket name for saving the pickle
        key (str): name of the key
        obj (_type_): object file
    """
    try:
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=obj)
        msg = f"save the object to bucket_name: {bucket_name}, key: {key}"
        logger.info(msg, extra={"tags": {"module": "common"}})
    except Exception as e:
        msg = f"can NOT save object to bucket_name: {bucket_name}, key: {key}. exception: {e}"
        logger.error(msg, extra={"tags": {"module": "common"}})
        sys.exit(1)


def save_pickle_to_s3(s3_client: Client, bucket_name: str, key: str, obj):
    """Save model's pickle in S3
    Args:
        s3_client (Client): client connection to Amazon S3
        bucket_name (str): bucket name for saving the pickle
        key (str): name of the key
        obj (_type_): pickle object
    """
    try:
        pickle_in = pickle.dumps(obj)
        save_to_s3(s3_client, bucket_name, key, pickle_in)
        msg = f"save the object to bucket_name: {bucket_name}, key: {key}"
        logger.info(msg, extra={"tags": {"module": "common"}})
    except Exception as e:
        msg = f"can NOT save pickle object to bucket_name: {bucket_name}, key: {key}. exception: {e}"
        logger.error(msg, extra={"tags": {"module": "common"}})
        sys.exit(1)


def load_from_s3(s3_client: Client, bucket_name: str, key: str) -> object:
    """Load object file from S3 Amazon
    Args:
        s3_client (Client): client connection to Amazon S3
        bucket_name (str): bucket name
        key (str): key name
    Returns:
        object: saved file as an object
    """
    msg = f"load object from s3: bucket_name: {bucket_name}, key: {key}"
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=key)
        logger.info(msg, extra={"tags": {"module": "common"}})
        return obj
    except Exception as e:
        msg = f"can NOT load object from s3: bucket_name: {bucket_name}, key: {key}. exception: {e}"
        logger.error(msg, extra={"tags": {"module": "common"}})
        sys.exit(1)


def load_pickle_from_s3(s3_client: Client, bucket_name: str, key: str) -> object:
    """Load pickle from Amazon S3
    Args:
        s3_client (Client): client connection to Amazon S3
        bucket_name (str): bucket name
        key (str): key name
    Returns:
        object: saved pickle file as an object
    """
    try:
        obj = load_from_s3(s3_client, bucket_name=bucket_name, key=key)
        unpickle_obj = pickle.loads(obj["Body"].read())
        msg = f"load pickle object from s3: bucket_name: {bucket_name}, key: {key}"
        logger.info(msg, extra={"tags": {"module": "common"}})
        return unpickle_obj
    except Exception as e:
        msg = f"can NOT load pickle object from s3: bucket_name: {bucket_name}, key: {key}. exception: {e}"
        logger.error(msg, extra={"tags": {"module": "common"}})
        sys.exit(1)