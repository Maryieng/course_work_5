import psycopg2


class DBManager():

    def __init__(self, database_name, params):
        self.name = database_name
        self.params = params
        self.create_database()
        self.create_table_companies()
        self.create_table_vacancies()


    def create_database(self):
        conn = psycopg2.connect(**self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self.name}")
        cur.execute(f'CREATE DATABASE {self.name}')

        conn.close()

        self.params.update({'dbname': self.name})

    def create_table_companies(self):
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE companies (
            supplier_id integer PRIMARY KEY,
            company_name varchar(150),
            contact varchar(150),
            address varchar(150),
            phone varchar(150),
            fax varchar(150),
            homepage varchar(150)
        )''')
        conn.commit()

        cur.close()
        conn.close()


    def create_table_vacancies(self):
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE vacancies (
            supplier_id integer PRIMARY KEY,
            company_name varchar(150),
            contact varchar(150),
            address varchar(150),
            phone varchar(150),
            fax varchar(150),
            homepage varchar(150)
        )''')
        conn.commit()

        cur.close()
        conn.close()


    def insert_data(self, table, data):
        pass

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass
