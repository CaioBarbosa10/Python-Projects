import requests
from twilio.rest import Client


STOCK_NAME = "BTC"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "7U8YTJVQD59O3ZY2"
NEWS_API_KEY = "f5a6d3bf3441467cb8076cd3199bbeaf"
TWILIO_SID = "AC611d186bf537cc993e2b4106a51cf7e6"
TWILIO_AUTH_TOKEN = "0494013b093a64fb38186a46b71285b2"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}



response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_yesterday = data_list[1]
day_before_yesterday_closing_price =day_before_yesterday["4. close"]



difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))


up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

porcentage = round((difference/float(yesterday_closing_price)) * 100)
print(porcentage)

if abs(porcentage) > 10:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{porcentage}%\nHeadline: {article['title']} \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+12512903472",
            to="+5531993887269"

        )
