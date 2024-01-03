import requests
from datetime import datetime
import smtplib
import time
My_EMAIL = "caiocbarbosa7@gmail.com"
PASSWORD = "fkyzopzpujgwrlsj"
MY_LAT = -19.917299
MY_LONG = -43.934559


def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if iss_latitude in range(-24, -13) and iss_longitude in range(-48, -37):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(My_EMAIL,PASSWORD)
        connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL,msg="Subject:Look Up\n\nThe iss is above you in the sky.")





