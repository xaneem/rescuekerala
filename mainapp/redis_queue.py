import os

from redis import Redis
from rq import Queue

REDIS_URL = os.environ.get("REDIS_URL")


def get_sms_queue():
    return Queue(name="smsjob", connection=Redis(REDIS_URL))
