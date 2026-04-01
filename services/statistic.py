from databases.mongodb.client import mongo_client
from config.config import config


def get_top_searches(limit=5):
    collection = mongo_client.get_collection(config.MONGO_COLLECTION)

    query = [
        {
            "$group": {
                "_id": {"search_type": "$search_type",
                        "param": "$param"},
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": limit
        }
    ]

    return list(collection.aggregate(query))


def get_last_searches(limit=5):
    collection = mongo_client.get_collection(config.MONGO_COLLECTION)

    query = [

        {
            "$sort": {"timestamp": -1}
        },
        {
            "$group": {
                "_id": {"search_type": "$search_type",
                        "param": "$param"},
                "new_file": {"$first": "$$ROOT"}
            }
        },
        {
            "$replaceRoot": {"newRoot": "$new_file"}
        },
        {
            "$sort": {"timestamp": -1}
        },
        {
            "$limit": limit
        }
    ]

    return list(collection.aggregate(query))