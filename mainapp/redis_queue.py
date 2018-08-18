import os

from redis import Redis
from rq import Queue

redis_host = os.environ.get("REDIS_URL")
redis_port = os.environ.get("mainapp/views.py")
q = Queue(connection=Redis(host=redis_host, port=redis_port))
