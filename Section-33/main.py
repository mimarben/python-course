import requests
 
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response.json())
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(f"The International Space Station is currently at {longitude}, {latitude}.")