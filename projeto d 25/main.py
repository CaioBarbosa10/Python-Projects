import pandas


#with open("./weather_data.csv") as weather_file:
 #   new_weather_list = weather_file.readlines()

 #   print(new_weather_list)
"""
import csv

with open("./weather_data.csv") as data_file:
    new_date_file = csv.reader(data_file)
    temperatures = []
    for row in new_date_file:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)

"""
#data = pandas.read_csv("weather_data.csv")
"""
#print(data)
#print(data["temp"])
#data_dic = data.to_dict()
#print(data_dic)

data_list =data["temp"].to_list()
#print(len(data_list))


max_temp =data["temp"].max()
print(max_temp)

# get data in collumn
print(data["condition"])

print(data.condition)
"""

# get data in row

#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]

#print(monday.condition)
#monday_temp = monday.temp[0]
#monday_temp_f = monday_temp * 9/5  + 32
#print(monday_temp_f)


# create a dataframe from Scrath

"""
data_dict = {
    "students ": ["Amy", "James", "Angela"],
    "scores ": [76, 56, 65]


}

data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")

"""
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231104.csv")

grey_squirrels_len = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_len = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_len = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_len)
print(red_squirrels_len)
print(black_squirrels_len)

data_dict = {
    "Four Color": ["Gray", "Cinnamon", "Black" ],
    "Count": [grey_squirrels_len,red_squirrels_len, black_squirrels_len]
}
print(data_dict)


df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")