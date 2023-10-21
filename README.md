# CW5_HH__SQL_Database

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