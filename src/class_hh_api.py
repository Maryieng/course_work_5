import requests
import json

class HH_API():
    HH_API_URL = 'https://api.hh.ru/vacancies'

    def __init__(self):
        pass


    def get_all_vacancies(self, id):
        params = {'per_page': 100,
                  'employer_id': id
                  }
        response = requests.get(self.HH_API_URL, params)
        response_data = json.loads(response.text)

        if 'items' in response_data:
            return response_data['items']
        else:
            return []
