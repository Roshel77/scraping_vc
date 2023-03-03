from pymongo import MongoClient

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "vc"


class VcPipeline:

    def __init__(self):
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client[MONGO_DB]

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.update_one(item, {"$set": item}, upsert=True)
        print()
        return item
