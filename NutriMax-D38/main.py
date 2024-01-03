import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG ="80.5"
HEIGHT_CM ="185"
AGE ="29"

APP_ID = "95040e73"
API_KEY = "dc260e7d729eb24a235b1926bd49f889"

username = "caio"
password ="caiojoga10"

nutri_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/7a5329b85996617d042f79dba560aec0/workoutTracking/workouts"

exercise_test =input("Tell me which exercises you did:")

headers = {

    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":"0"

}


parameters = {
    "query":exercise_test,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutri_endpoint,json=parameters,headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(username,password))

    print(sheet_response.text)