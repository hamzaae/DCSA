from pymongo import MongoClient

# Your MongoDB URI
uri = "mongodb+srv://hamzaae:7cVLGsNmmUAnWgAv@cluster0.vpvqzd4.mongodb.net/?retryWrites=true&w=majority"

def connect_mongo(uri):
    """ Connect to MongoDB """
    client = MongoClient(uri)
    return client

def insert_one_data(client, data, db_name, collection_name):
    """ Insert one data into MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.insert_one(data)
    return result

def insert_many_data(client, data, db_name, collection_name):
    """ Insert many data into MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.insert_many(data)
    return result 

def find_one_data(client, db_name, collection_name):
    """ Find one data from MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.find_one()
    return result

def find_many_data(client, db_name, collection_name):
    """ Find many data from MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.find()
    return result

def get_one_data(client, db_name, collection_name, query):
    """ Get one data from MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.get(query)
    return result

def get_many_data(client, db_name, collection_name, query):
    """ Get many data from MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.get(query)
    return result
 

def get_all_data(client, db_name, collection_name):
    """ Get all data from MongoDB """
    db = client[db_name]
    collection = db[collection_name]
    result = collection.find()
    return result


if __name__ == "__main__":
    # Create a new client and connect to the server
    client = connect_mongo(uri)

    data_to_insert = {
      "comment": "Comment 1",
      "cleaned_comment": "Comment Cleaned 1",
      "stemmed_comment": "Comment Stemmed 1",
      "labels": [
        1,
        1,
        0
      ]
    }

    # insert_one_data(client, data_to_insert, "dcsa", "comments")

    cursor = find_many_data(client, "dcsa", "comments")

    for document in cursor:
        print(document.get("comment"))

    # Close the MongoDB connection
    client.close()

