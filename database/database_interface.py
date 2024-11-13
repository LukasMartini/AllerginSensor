import configparser
import psycopg2

config_parser = configparser.ConfigParser(allow_no_value=True)
config_parser.read('config.ini')

initialize_database_sql = config_parser.get('FILE_PATHS', 'initialize_database')

class database_interface:

    # All positional arguments are for deliniating which database to connect to and how.
    def __init__(self, dbname: str = None, username: str = None, 
                 password: str = None, host: str = None, port: str = None):
        self.conn = psycopg2.connect(dbname=dbname, user=username, password=password, host=host, port=port)
        self.curr = self.conn.cursor()

    def __del__(self):
        self.curr.close()
        self.conn.close()

    def initialize_database(self):
        with open(initialize_database_sql) as query:
            self.exec_query(query.read())


    def exec_query(self, query: str, fetch: bool = False, *inputs):
        if not inputs: # We love falsy values!
            self.curr.execute(query)
        else:
            self.curr.execute(query, inputs)
        self.conn.commit()
        
        if fetch:
            return self.curr.fetchall()
        else:
            return None