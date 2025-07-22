# Tasks

This document lists the development tasks to be completed.

- [x] **Task 1: Set up the project structure.**
    - [x] Create the `docs`, `src`, and `notebooks` directories.
    - [x] Create the `.gitignore` file.
    - [x] Move the markdown files to the `docs` directory.

- [x] **Task 2: Implement the `config.py` module.**
    - [x] Create the `src/config.py` file.
    - [x] Add code to load environment variables from a `.env` file (using `python-dotenv`).
    - [x] Define variables for eBay API credentials and the MongoDB connection string.
    - [x] Handle multiple search keywords.

- [x] **Task 3: Implement the `ebay_client.py` module.**
    - [x] Create the `src/ebay_client.py` file.
    - [x] Add a function to authenticate with the eBay API (with placeholder logic).
    - [x] Add a function to fetch item sales data for a given keyword (with simulated data).

- [x] **Task 4: Implement the `mongo_manager.py` module.**
    - [x] Create the `src/mongo_manager.py` file.
    - [x] Add a function to connect to the MongoDB database.
    - [x] Add a function to perform an "upsert" operation on the data.

- [x] **Task 5: Implement the `main.py` script.**
    - [x] Create the `src/main.py` file.
    - [x] Import the necessary modules (`config`, `ebay_client`, `mongo_manager`).
    - [x] Add the main logic to call the eBay API and store the data in MongoDB.

- [x] **Task 6: Create a test notebook.**
    - [x] Create the `notebooks/api_test.ipynb` file.
    - [x] Add code to test the eBay API connection and data fetching.

- [x] **Task 7: Set up dependencies.**
    - [x] Create a `Pipfile` to manage dependencies (`python-dotenv`, `pymongo`, `requests`).

- [ ] **Task 8: Final Configuration and Testing.**
    - [ ] Create a `.env` file from the `.env.example` template.
    - [ ] Add your eBay API credentials and MongoDB connection string to the `.env` file.
    - [ ] Update the placeholder OAuth logic in `src/ebay_client.py` with the real implementation once credentials are available.
    - [ ] Run the full pipeline with `pipenv run python -m src.main` to perform an end-to-end test.

- [ ] **Task 9: Deployment.**
    - [ ] Write instructions on how to deploy the project to Render as a scheduled task.
