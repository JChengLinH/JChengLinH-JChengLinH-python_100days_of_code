import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_endpoint: str, sheet_token: str):
        self.sheet_endpoint = sheet_endpoint
        self.sheet_headers = {"Authorization": sheet_token}

        sheet_response = requests.get(url=self.sheet_endpoint, headers=self.sheet_headers)
        sheet_response.raise_for_status()
        sheet_data = sheet_response.json()
        

        self.city_list=[]
        for city in sheet_data["prices"]:
            city_dict = {key: value for (key, value) in city.items() if key == "city" or key == "id" or key == "lowestPrice"}
            self.city_list.append(city_dict)


    def write_sheet_data(self, iata_code: str, price: int, obj_id: int):
        sheet_post_params = {
            "price":{
                "iataCode": iata_code,
                "lowestPrice": price,
            }
        }
        sheet_response = requests.put(url=f"{self.sheet_endpoint}/{obj_id}", json=sheet_post_params, headers=self.sheet_headers)
        sheet_response.raise_for_status()