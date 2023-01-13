from redis import Redis
from app.config import Config

r = Redis(host=Config.REDIS_HOST,
          port=Config.REDIS_PORT,
          db=Config.REDIS_DB)


def init():
    r.set("Organization", "KhAI")
    r.set("Department", "College")
    r.set("Course", "DevOps")


def add_key(key, value):
    r.set(key, value)


def get_key(key):
    return r.get(key)
