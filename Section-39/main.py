from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import time

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.read_data()
pprint(sheet_data)

for row in sheet_data['prices']:
    pprint(row)
    if row["idIata"] == "":
        print(f"**********************************************",row["city"])
        row["idIata"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
#data_manager.update_destination_codes()

#data_manager.write_price(2,76,"Edinburgh")