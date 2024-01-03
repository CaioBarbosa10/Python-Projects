import requests
from datetime import datetime
MY_LAT = -19.917299
MY_LNG = -43.934559

parameters = {
    "formatted": 0,
    "lat": MY_LAT,
    "lng": MY_LNG

}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)




