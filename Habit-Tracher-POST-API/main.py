import requests
from datetime import datetime

TOKEN="aushasuu824aksy"
USER_NAME="caiobarbosa"
PIXELA_ENDPOINT ="https://pixe.la/v1/users"
GRAPH_ID ="graph-07"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)

GRAPH_ENDPOINT =f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_config = {

    "id":"graph-07",
    "name":"Running Graph",
    "unit":"km",
    "type":"float",
    "color":"shibafu"

}

headers ={

    "X-USER-TOKEN":TOKEN
}

#response = requests.post(url=GRAPH_ENDPOINT,json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint =f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_data = {

    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you run today ?")

}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
#print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{pixel_data['date']}"
#response = requests.put(url=pixel_update_endpoint,json=pixel_data,headers=headers)
#print(response.text)

delete_endpoint = pixel_update_endpoint
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)
