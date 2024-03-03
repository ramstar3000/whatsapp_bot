from pymongo.mongo_client import MongoClient
import pandas as pd

username = "Ram"
password = "Ram"

uri = f"mongodb+srv://{username}:Ram@cluster0.qedvh8z.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

database_name = "Whatsapp"
cluster_name = "Cluster0"

# Access the database

db = client[database_name]

# Access the table Bot

collection = db["Bot"]

# Read the data from the table into a json

data = collection.find()

# Convert the json into a pandas dataframe

df = pd.DataFrame(list(data))

print(df)