import requests

api_key = "341cba64efea2dc1a7330b94d1ec712a"

MY_LAT = -19.917299
MY_LNG = -43.934559

parameters = {

    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key

}
response = requests.get("https://api.openweathermap.org/data/2.5/weather",params=parameters)
response.raise_for_status()
data = response.json()
print(data)
