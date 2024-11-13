import os
import configparser

from database.database_interface import database_interface

from server.server import activate_server
from server.amqp_data_extractor import amqp_data_extractor
from server.data_outputter import data_printer

config_parser = configparser.ConfigParser(allow_no_value=True)
config_parser.read('config.ini')

DBNAME = config_parser.get('DATABASE_ACCESS', 'DBNAME')
USERNAME = config_parser.get('DATABASE_ACCESS', 'USERNAME')
PASSWORD = config_parser.get('DATABASE_ACCESS', 'PASSWORD')
HOST = config_parser.get('DATABASE_ACCESS', 'HOST')
PORT = config_parser.get('DATABASE_ACCESS', 'PORT')

INIT_DB = config_parser.get('STARTUP_PARAMETERS', 'INIT_DB')

def main():

    # Create application-specific objects
    outputter = data_printer()
    extractor = amqp_data_extractor(outputter)
    interface = database_interface(dbname=DBNAME, username=USERNAME, password=PASSWORD, host=HOST, port=PORT)

    if INIT_DB:
        interface.initialize_database()

main()
