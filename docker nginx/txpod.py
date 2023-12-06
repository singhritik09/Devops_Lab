import requests
import json
import time
import os
# Define the JSON data to send
json_data = {
    "key1": "value1",
    "key2": "value2"
}

url = "http://commrecv:5000/receive_json"

headers = {
    'Content-Type': 'application/json'
}
message_frequency = int(os.environ.get("freq", 10))
while (True):

    response = requests.post(url, headers=headers, data=json.dumps(json_data))

    if response.status_code == 200:
        print("JSON message sent successfully")
    else:
        print("Failed to send JSON message")
    time.sleep(message_frequency)
