from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import pytz
import os
load_dotenv()
hkConnectionString= os.getenv("HK_DB_STRING")
# connection to this db requires ZTNA access but streamlit pe ZTNA ke saath its not working 

def insert_to_db(data , database , collection):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Update the connection string with your MongoDB URI
    db = client[database]  # Replace "mydatabase" with your database name
    collection = db[collection]  # Replace "mycollection" with your collection name
    # Insert data into MongoDB collection
    collection.insert_one(data)
    print("Data inserted successfully!")
