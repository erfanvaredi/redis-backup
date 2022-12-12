from logging import getLogger

from boto3 import client
from boto3_type_annotations.s3 import Client as S3Client
from src.packages.utils import save_pickle_to_s3
import settings

logger = getLogger(__name__)
logger.addHandler(settings.handler)


def run(s3_client: S3Client):
    
    if settings.DEBUG is False:
        save_pickle_to_s3(
            s3_client=s3_client,
            bucket_name=settings.AWS_BUCKET_NAME,
            key='something.pickle',
            obj=,
        )


    # logger.info("learning process just FINISHED", extra={"tags": {"module": "learner"}})


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

    run(s3_client)