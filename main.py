from src.class_hh_api import HH_API
from src.class_DBManager import DBManager
from pprint import pprint


def main():
    hh_api = HH_API()
    vacancies = hh_api.get_vacancies()
    pprint(vacancies)

    db_manager = DBManager()


if __name__ == "__main__":
    main()
