
import requests
from dotenv import load_dotenv
import os
import credits

def configure():
    load_dotenv()


# GET request made for response
# configure()
response = requests.get(f"https://httpsecond.azurewebsites.net/api/httpsecond?code={credits.url_key}")
# print (f"https://httpsecond.azurewebsites.net/api/httpsecond?code={credits.url_key}")
# Checking for the successful execution of the function
if response.status_code == 200: 
    # getting the response thro JSON
    data = response.json()
    print("Response data:", data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print("inside else statement")

    