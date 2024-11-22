import azure.functions as func
import logging
import os
from azure.cosmos import CosmosClient, exceptions
from azure.cosmos.partition_key import PartitionKey
import json



#adding connection string to the function
connectionString = os.environ["AzureConnectionString"]
client = CosmosClient.from_connection_string(connectionString)


# database, container and item details
databaseName = "resumedbid"
containerName = "containerid"
itemId = "1"

# getting database and container names
database = client.get_database_client(databaseName)
container = database.get_container_client(containerName)

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.function_name (name="httpsecond")
@app.route(route="httpsecond")
def httpsecond(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:

        #defining the query to retrive item from the container table
        query = f"SELECT * FROM c WHERE c.id = '1'"

        items = list(container.query_items(query=query,enable_cross_partition_query=True))
        if not items:
            return func.HttpResponse("Item not found", status_code=404)
        
        #incrementing the count value in the container table item
        item = items[0]
        countnow = int(item.get('count',0))

        #incrementing the count
        newcount = countnow + 1
        item['count'] = newcount

        #updating the count in the table
        container.upsert_item(item)

        # updating in the json file
        item_json = json.dumps(item, indent=2)

        # returing the new item as Json response
        return func.HttpResponse(body=json.dumps({"count":newcount}), 
                mimetype = 'application/json',status_code = 200 )
    
    except exceptions.CosmosHttpResponseError as e: 
        logging.error(f"An error occurred: {e.message}") 
        return func.HttpResponse( f"An error occurred: {e.message}", status_code=500)

   