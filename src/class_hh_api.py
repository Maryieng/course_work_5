import requests
import json

class HH_API():
    HH_API_URL = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.params = {
            'per_page': 100
        }
    def get_vacancies(self):
        response = requests.get(self.HH_API_URL, self.params)
        response_data = json.loads(response.text)
        if 'items' in response_data:
            return response_data['items']
        else:
            return []