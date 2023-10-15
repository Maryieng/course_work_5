import json
from src.class_hh_api import HH_API
from pprint import pprint

FILENAME = 'companies.json'


def load_companies():
    pass


def load_jsonfile(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result


def load_all_vacancies_from_company(id):
    hh_api = HH_API()
    vacancies = hh_api.get_vacancies()
    pprint(vacancies)
