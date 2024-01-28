Данный проект позволяет получать данные о работодателях и их вакансиях с сайта hh.ru. 
Для этого используйте публичный API hh.ru и библиотеку запросов. 
Проект определяет 10 крупнейших ИТ-компаний России. Данные о вакансиях и работодателях добавляются в таблицы базы данных PostgreSQL. 
Для работы с базой данных используется библиотека — psycopg2. 
Для работы с базой данных используется класс DBManager. 
Перед началом необходимо установить библиотеки из «requirements.txt». 
Также нужно создать файл «database.ini» в каталоге «data» для работы с локальной базой данных.

Класс DBManager имеет следующие методы:

get_companies_and_vacancies_count() — получает список всех компаний и количество вакансий для каждой компании. 
get_all_vacancies() — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты, а также ссылку на вакансию. 
get_avg_salary() — получает среднюю зарплату по вакансиям. 
get_vacancies_with_higher_salary() — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. 
get_vacancies_with_keyword() — получает список всех вакансий, заголовки которых содержат слова, переданные в метод, например python.


English version

This project allows you to obtain data about employers and their vacancies from the site hh.ru. 
To do this, use the public API hh.ru and the requests library.
The project predetermines the 10 largest IT companies in Russia.
Job vacancy and employer data is added to tables in the PostgreSQL database. 
A library is used to work with the database - psycopg2
To work with the database, use the class DBManager.
Before starting, you need to install the libraries from the 'requirements.txt'.
You need to create a file 'database.ini' in directory 'data' to work with your local database.

Class DBManager have the following methods:

get_companies_and_vacancies_count()
  — gets a list of all companies and the number of vacancies for each company.
get_all_vacancies()
  — receives a list of all vacancies indicating the company name, vacancy title and salary, and a link to the vacancy.
get_avg_salary()
  — receives the average salary for the vacancies.
get_vacancies_with_higher_salary()
  — gets a list of all vacancies whose salary is higher than the average for all vacancies.
get_vacancies_with_keyword()
  — gets a list of all vacancies whose titles contain the words passed to the method, for example python.
