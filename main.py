from src.class_hh_api import HH_API
from src.class_DBManager import DBManager
from src.utils import load_companies, load_all_vacancies_from_company, config
from pprint import pprint


def main():

    database_name = 'hh_vacancies'
    file_companies_ids = 'data/companies.json'

    companies = load_companies(file_companies_ids)
    pprint(companies)

    params = config()

    #db_manager = DBManager(database_name, params)
    #print(f'База SQL {db_manager.name} создана')

    hh_api = HH_API()

    #for vacancy in vacancies:
    #    if 'лига' in vacancy['employer']['name'].lower():
    #        print(f"{vacancy['employer']['name']} - {vacancy['employer']['id']}")

    for company in companies:
        #company_info = hh_api.get_company_info()
        vacancies = hh_api.get_all_vacancies(company['id'])
        print(f"Компания {company['name']} - количество вакансий", len(vacancies))





if __name__ == "__main__":
    main()
