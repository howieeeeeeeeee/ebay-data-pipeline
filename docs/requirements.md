# Requirements

## **Project Overview: eBay Data Pipeline**

### **Main Goal** 

The primary goal of this project is to create an automated daily job that fetches item sales data from the **eBay Marketplace Insights API** using a specific keyword. The retrieved data will be stored in a **MongoDB** database, with a mechanism to prevent duplicates by updating existing records if they are fetched again (an "upsert" operation). The entire process will be deployed as a scheduled task on a cloud service like **Render**.

---

### **Project Folder Structure** 

This is the finalized folder structure designed to be organized, scalable, and secure.

```
ebay-data-pipeline/
├── .env
├── .gitignore
├── docs/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
├── notebooks/
│   └── api_test.ipynb
├── src/
│   ├── config.py
│   ├── ebay_client.py
│   ├── mongo_manager.py
│   └── main.py
├── Pipfile
└── Pipfile.lock
```



**`.gitignore` Configuration** 

- This file tells Git which files and folders to ignore. As you requested, we will ensure it's configured correctly from the start.
    
- **Contents for `.gitignore`:**
    
    Code snippet
    
    ```
    # Environment variables - NEVER commit secrets
    .env
    
    # Jupyter Notebook files and checkpoints
    *.ipynb
    .ipynb_checkpoints/
    
    # Python specific
    __pycache__/
    *.pyc
    
    # IDE / Editor configuration
    .vscode/
    .idea/
    ```



### Folder Explanation

- **`docs/` (Documentation)** 
    
    - This folder will contain the three specification files you mentioned:
        
        - **`requirements.md`**: What the system should do.
            
        - **`design.md`**: How the system will be built.
            
        - **`tasks.md`**: The specific steps to build it.