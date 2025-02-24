import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
# Load environment variables from .env file
load_dotenv()

SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
SHEET_NAME = "prices"
class DataManager:
    def __init__(self):
        self._user = os.environ["ENV_SHEETY_USERNAME"]
        self._password = os.environ["ENV_SHEETY_PASSWORD"]
        self._sheety_token = os.environ["ENV_SHEETY_TOKEN"]
        self._auth = HTTPBasicAuth(self._user, self._password)
        self._headers = {
            #"Authorization": f"Bearer {SHEETY_TOKEN}",
            "Content-Type": "application/json"
        }
        self.destination_data = {}
    
    def read_data(self):
        try:
            response = requests.get(SHEETY_ENDPOINT, auth=self._auth, headers=self._headers)    
            # Raise an exception if the request failed
            response.raise_for_status()    
            data = response.json()
            self.destination_data = response.json()
            return self.destination_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return None

    def write_price(self,row_id, new_price, city):
        update_endpoint =f"{SHEETY_ENDPOINT}/{row_id}"
        payload = {
            "price": {
                "lowPrice": new_price,
                "city": city,
            }
        }        
        try:
            # Make PUT request to update the row
            response = requests.put(
                url=update_endpoint,
                json=payload,
                auth=self._auth,
                headers=self._headers
            )            
            # Raise an exception if the request failed
            response.raise_for_status()            
            print(f"Successfully updated {city} lowest price to ${new_price}")
            return response.json()            
        except requests.exceptions.RequestException as e:
            print(f"Error updating price: {e}")
            return None
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "idIata": city["idIata"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)