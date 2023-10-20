import json
from configparser import ConfigParser
import os


def config(filename: str = "data/database.ini", section: str = "postgresql"):
    """
    This function for getting parameters of database
    :param filename:str
    :param section:str
    :return:dict
    """

    # create a parser
    path_absolute = os.path.abspath(filename)
    parser = ConfigParser()

    # read config file
    parser.read(path_absolute)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


def load_companies(filename: str):
    """
    This function for getting companies from file
    :param filename: str
    :return: dict
    """
    result = load_jsonfile(filename)
    return result


def load_jsonfile(filename: str):
    """
    This function for load data from json file
    :param filename: str
    :return: dict
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result
