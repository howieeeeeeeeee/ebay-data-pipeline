from pymongo import MongoClient, UpdateOne
from src.config import config

class MongoManager:
    """
    Manages the connection and data operations with MongoDB.
    """
    def __init__(self):
        if not config.MONGO_URI:
            raise ValueError("MONGO_URI not set in environment variables.")
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client.get_default_database() # Or specify a db name
        self.collection = self.db.ebay_items

    def upsert_items(self, items):
        """
        Performs a bulk upsert operation for a list of items.
        """
        if not items:
            print("INFO: No items to upsert.")
            return

        operations = []
        for item in items:
            # Use 'itemId' as the unique identifier for the upsert operation
            filter_query = {'itemId': item['itemId']}
            update_query = {'$set': item}
            operations.append(UpdateOne(filter_query, update_query, upsert=True))

        print(f"INFO: Upserting {len(operations)} items into MongoDB.")
        result = self.collection.bulk_write(operations)
        print(f"INFO: MongoDB bulk write result: {result.bulk_api_result}")

    def close_connection(self):
        """
        Closes the MongoDB connection.
        """
        self.client.close()
