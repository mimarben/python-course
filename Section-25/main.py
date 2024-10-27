import csv
import pandas as pnd


with open("Section-25/weather_data.csv") as file:
    data = file.readlines()
    print(data)
    
with open("Section-25/weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    
data = pnd.read_csv("Section-25/weather_data.csv")
print(data)
print(type(data))
print((data["temp"].mean()).round(1))
print((data["temp"].max()).round(1))
print(data.temp.max().round(1))

print(data[data.temp == data.temp.max()])


data_dict = {
    "sudents": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pnd.DataFrame(data_dict)