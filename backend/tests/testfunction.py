
import requests

# GET request made for response
print("I am before the url")
response = requests.get("https://httpsecond.azurewebsites.net/api/httpsecond?code=4Ydrtk3miGpE4Vn9T6LkXTXiyXrZkfBjLHiNg_YOBwEGAzFuIMQ7tQ%3D%3D")

# Checking for the successful execution of the function
if response.status_code == 200: 
    # getting the response thro JSON
    data = response.json()
    print("Response data:", data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print("inside else statement")

    