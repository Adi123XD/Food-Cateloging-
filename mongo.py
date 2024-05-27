from pymongo import MongoClient

def insert_to_db(data , database , collection):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Update the connection string with your MongoDB URI
    db = client[database]  # Replace "mydatabase" with your database name
    collection = db[collection]  # Replace "mycollection" with your collection name
    # Insert data into MongoDB collection
    collection.insert_one(data)
    print("Data inserted successfully!")
