import logging
import logging.config
import os
import time
from ast import literal_eval
from functools import lru_cache
from pathlib import Path

import logging_loki
from dotenv import load_dotenv
from pydantic import BaseModel, BaseSettings, StrictStr, ValidationError, validator

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

VERSION = os.getenv("VERSION")

SERVICE_NAME = "basi"
SERVICE_VERSION = "v" + os.getenv("VERSION")

DEBUG = literal_eval(os.getenv("DEBUG", "true").capitalize())


# =======================================
# CONFIGS
REDIS_PASS = os.getenv("CONFIG_REDIS_PASS")
# =======================================


# logging
BASE_LOGGING_ENDPOINT = os.getenv("BASE_LOGGING_ENDPOINT")
if BASE_LOGGING_ENDPOINT:
    logging_loki.emitter.LokiEmitter.level_tag = "level"
    handler = logging_loki.LokiHandler(
        url=f"{BASE_LOGGING_ENDPOINT}/loki/api/v1/push",
        tags={"application": "redis-backup"},
        version="1",
    )
else:
    handler = logging.StreamHandler()
    handler.setLevel(level=20)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": '{ "level": "%(levelname)s", "time": "%(asctime)s","filename": %(filename)s, "function_name": %(funcName)s, "line_number":%(lineno)d, "message": %(message)s }',
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


logging.config.dictConfig(LOGGING)
logging.Formatter.converter = time.gmtime

logging.addLevelName(logging.ERROR, "error")
logging.addLevelName(logging.WARNING, "warning")
logging.addLevelName(logging.INFO, "info")
logging.addLevelName(logging.DEBUG, "debug")

logging.getLogger("redis-backup").setLevel(logging.ERROR)
