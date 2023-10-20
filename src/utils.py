import json
from src.class_hh_api import HH_API
from pprint import pprint
from configparser import ConfigParser
import os


def config(filename="data/database.ini", section="postgresql"):
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


def load_companies(filename):
    result = load_jsonfile(filename)
    return result


def load_jsonfile(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result
