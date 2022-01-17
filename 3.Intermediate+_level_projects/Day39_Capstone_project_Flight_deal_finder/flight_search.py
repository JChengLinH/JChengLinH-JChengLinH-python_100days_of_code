from locale import currency
from re import search
import requests
from data_manager import DataManager
import datetime as dt
from dateutil.relativedelta import relativedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, sheet_endpoint: str, sheet_token: str, kiwi_token: str):
        self.kiwi_endpoint = "https://tequila-api.kiwi.com"
        self.kiwi_api_key = kiwi_token
        self.kiwi_headers = {"apikey": self.kiwi_api_key}
        self.sheet = DataManager(sheet_endpoint, sheet_token)
        self.iata_code = []
    

    def fetch_iata_code(self) -> list:
        kiwi_location_endpoint = f"{self.kiwi_endpoint}/locations/query"
        for city in self.sheet.city_list:

            kiwi_location_params = {
                "term": city["city"],
                "location_types": "airport",
            }

            kiwi_response = requests.get(url=kiwi_location_endpoint, params=kiwi_location_params, headers=self.kiwi_headers)
            kiwi_response.raise_for_status()
            self.iata_code.append(kiwi_response.json()["locations"][0]["code"])
        
        return self.iata_code
    

    def search_flights(self, from_iata_code: str, to_iata_codes: list) -> list:
        kiwi_search_endpoint = f"{self.kiwi_endpoint}/v2/search"
        destinations = ",".join(to_iata_codes)

        kiwi_search_params = {
            "fly_from": from_iata_code,
            "fly_to": destinations,
            "date_from": (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (dt.datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y"),
            "ret_from_diff_airport": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "EUR"
            "one_for_city": 1,
            "max_stopovers": 2,
            "vehicle_type": "aircraft",
        }

        kiwi_response = requests.get(url=kiwi_search_endpoint, params=kiwi_search_params, headers=self.kiwi_headers)
        kiwi_response.raise_for_status()
        search_result = kiwi_response.json()
        
        return search_result


        


