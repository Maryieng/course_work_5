from src.class_hh_api import HH_API
from src.class_DBManager import DBManager
from src.utils import load_companies, config
from pprint import pprint
from src.class_vacancy import Vacancy


def main():

    database_name = 'hh_vacancies'
    file_companies_ids = 'data/companies.json'

    companies = load_companies(file_companies_ids)

    params = config()

    db_manager = DBManager(database_name, params)
    print(f'База SQL {db_manager.name} создана')

    hh_api = HH_API()

    for company in companies:

        vacancies_info = hh_api.get_all_vacancies(company['id'])
        db_manager.insert_data_company(vacancies_info[0])

        vacancies = []
        for vacancy_info in vacancies_info:
            vacancy = Vacancy.create_vacancy_from_hh(vacancy_info)
            vacancies.append(vacancy)

        db_manager.insert_data_vacancy(vacancies)

        print(f"Компания {company['name']} - количество вакансий", len(vacancies_info))
    print('Данные по вакансиям выбранных работодателей добавлены в базу данных SQL')

    while True:

        print('''
Добрый день!
Выберите один из пунктов
1 - получить список всех компаний и количество вакансий у каждой компании
2 - получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
3 - получить среднюю зарплату по вакансиям
4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
5 - получить список всех вакансий, в названии которых содержится слово python
0 - выход''')

        user_input = input()
        if user_input == "1":
            db_manager.get_companies_and_vacancies_count()
        elif user_input == "2":
            db_manager.get_all_vacancies()
        elif user_input == "3":
            db_manager.get_avg_salary()
        elif user_input == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif user_input == "5":
            db_manager.get_vacancies_with_keyword('python')
        elif user_input == "0":
            break
        else:
            print('Неверная команда')

if __name__ == "__main__":
    main()

    #[postgresql]
    #host = localhost
    #user = postgres
    #password = 1985
    #port = 5432
