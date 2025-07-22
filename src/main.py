from src.config import config
from src.ebay_client import EbayClient
from src.mongo_manager import MongoManager

def main():
    """
    Main function to run the eBay data pipeline.
    """
    print("INFO: Starting eBay data pipeline...")
    ebay_client = EbayClient()
    mongo_manager = MongoManager()

    all_items = []
    for keyword in config.SEARCH_KEYWORDS:
        try:
            data = ebay_client.search_item_sales(keyword)
            if data and 'itemSales' in data:
                all_items.extend(data['itemSales'])
        except Exception as e:
            print(f"ERROR: Failed to fetch data for keyword '{keyword}': {e}")

    if all_items:
        try:
            mongo_manager.upsert_items(all_items)
        except Exception as e:
            print(f"ERROR: Failed to upsert data to MongoDB: {e}")

    mongo_manager.close_connection()
    print("INFO: eBay data pipeline finished.")

if __name__ == "__main__":
    main()
