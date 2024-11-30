import azure.functions as func
import logging
import os
from azure.cosmos import CosmosClient, exceptions
from azure.cosmos.partition_key import PartitionKey
import json
import requests
import credits

#adding connection string to the function
connectionString = os.environ["AzureConnectionString"]
#(f"echo AzureConnectionString = {AzureConnectionString}")


client = CosmosClient.from_connection_string(connectionString)


# database, container and item details
databaseName = "resumedbid"
containerName = "containerid"
itemId = "1"

# getting database and container names
database = client.get_database_client(databaseName)
container = database.get_container_client(containerName)

# Getting database and container clients
database = client.get_database_client(databaseName)
container = database.get_container_client(containerName)

def get_cosmosdbcount() -> int:
    count_item = container.read_item(itemId, partition_key=itemId)
    current_count = count_item.get('count', 0)
    return current_count
    
def test_resume_counter():
    initial_count = get_cosmosdbcount()

    # Increment count in Cosmos DB with a new API call
    req = requests.get(f"https://httpsecond.azurewebsites.net/api/httpsecond?code={credits.url_key}")
    #response = requests.get(f"https://httpsecond.azurewebsites.net/api/httpsecond?code={credits.url_key}")

    httpsecond(req)

    new_count = get_cosmosdbcount()
    
    # If new_count is greater than initial_count, then our test passed
    print(f"Initial Count: {initial_count} | New Count: {new_count}")
    assert new_count > initial_count
