
import csv

    # with open("weather_data.csv") as file:
    #     data = csv.reader(file)
    #     temperature = []
    #     for row in data:
    #         if row[1] != "temp":
    #             temperature.append(int(row[1]))
    #     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].tolist()
# mean_data = data["temp"].mean()
# max_val = data["temp"].max()
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = (monday_temp * 9/5)+32
# print(monday_temp_F)

# creating dataframes from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict={
    "Fur color":["Grey", "Cinnamon", "Black"],
    "Count":[grey_squirrels, Cinnamon_squirrels, Black_squirrels]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")


