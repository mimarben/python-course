import requests
import pandas as pd
import os


API_KEY=os.environ.get('API_KEY_OW')
print(f'MY_VARIABLE: {API_KEY}')

LATITUDE=41.652252
LONGITUDE=  -4.724532
UNITS= "metric"
CITY='Valladolid,ES'
URL_LAT_LONG=f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&units={UNITS}&appid={API_KEY}"
URL_CITY= f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}'
FORECAST_LAT_LONG=f"https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&units={UNITS}&appid={API_KEY}"
response= requests.get(URL_LAT_LONG)
response.raise_for_status()
data = response.json()
""" print(data)
print("************************************************")
print(URL_CITY)
print("************************************************")
city_data = requests.get(URL_CITY)
city_data.raise_for_status()
city_weather_data = city_data.json()
print(city_weather_data) """
print("************************************************")
print(FORECAST_LAT_LONG)
print("************************************************")
forecast_data = requests.get(FORECAST_LAT_LONG)
forecast_data.raise_for_status()
forecast_weather_data = forecast_data.json()
df= pd.json_normalize(forecast_weather_data["list"])
print(df)
for index, row in df.iterrows():
    if row["weather"][0]["id"]>=500 and row["weather"][0]["id"]<=531:
        print(f"Date: {row['dt_txt']} - Temperature: {row['main.temp']}°C - Description: {row['weather'][0]['description']}")
        print(row["weather"][0]["id"])
    else:
        print("not rainy")
#    print(f"Date: {row['dt_txt']} - Temperature: {row['main.temp']}°C - Description: {row['weather'][0]['description']}")
