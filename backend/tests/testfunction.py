
import requests

# GET request made for response
print("I am before the url")


# Checking for the successful execution of the function
if response.status_code == 200: 
    # getting the response thro JSON
    data = response.json()
    print("Response data:", data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print("inside else statement")

    