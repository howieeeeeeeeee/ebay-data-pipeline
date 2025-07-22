# Design

This document outlines the technical design of the project.

## System Architecture

The system will be composed of several Python modules working together to achieve the desired functionality.

- **`main.py`**: The entry point of the application. It will orchestrate the entire process of fetching data from the eBay API and storing it in MongoDB.
- **`ebay_client.py`**: This module will be responsible for all interactions with the eBay Marketplace Insights API. It will handle authentication and data fetching.
- **`mongo_manager.py`**: This module will manage the connection to the MongoDB database and handle the data insertion and update (upsert) operations.
- **`config.py`**: This module will manage the configuration of the application, including API keys and database connection strings. It will load these values from a `.env` file.

## Data Flow

1. The `main.py` script will be executed daily by a scheduler (e.g., Render Cron Job).
2. `main.py` will call the `ebay_client.py` module to fetch the item sales data for the specified keyword.
3. The `ebay_client.py` module will make a request to the eBay API and return the data.
4. `main.py` will then pass the retrieved data to the `mongo_manager.py` module.
5. The `mongo_manager.py` module will connect to the MongoDB database and perform an "upsert" operation to either insert a new document or update an existing one based on a unique identifier from the eBay data.

## API Specification

The application will use the `search` method of the eBay Marketplace Insights API. The specific endpoint and parameters will be detailed in the `ebay_client.py` module.