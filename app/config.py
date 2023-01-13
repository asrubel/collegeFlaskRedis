from os import getenv
from dotenv import load_dotenv

load_dotenv('.env.list')


class Config:
    REDIS_PORT = getenv('REDIS_PORT')
    REDIS_DB = getenv('REDIS_DB')
    REDIS_HOST = getenv('REDIS_HOST')
