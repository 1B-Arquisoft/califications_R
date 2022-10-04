import pymongo
from decouple import config

uri = config('URI')

client = pymongo.MongoClient(uri)

def connect(collection):
    result = client["ArquiSoft"][collection]
    return result