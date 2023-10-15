from src.class_hh_api import HH_API
from src.class_DBManager import DBManager
from src.utils import load_companies, load_all_vacancies_from_company
from pprint import pprint


def main():

    companies = load_companies()
    for company in companies:
        vacancies = load_all_vacancies_from_company(company['id'])




    db_manager = DBManager()


if __name__ == "__main__":
    main()
