import requests
from datetime import datetime
MY_LAT=41.639093001050504
MY_LONG= -4.743937266586598

parameters = {"lat":MY_LAT,"lng":MY_LONG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"The sunrise time in your location is: {sunrise}")
print(f"The sunset time in your location is: {sunset}")



print(data)