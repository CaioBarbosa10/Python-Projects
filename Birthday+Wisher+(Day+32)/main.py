import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "caiocbarbosa7@gmail.com"
PASSWORD = "fkyzopzpujgwrlsj"

today = dt.datetime.now()


today_tuple =(today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    random_number = random.randint(1,3)
    file_path = f"letter_templates/letter_{random_number}.txt"
    with open(f"{file_path}") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}"
                            )



