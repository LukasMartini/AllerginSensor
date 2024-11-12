import psycopg2

class database_interface:

    def __init__(self, dbname: str = None, username: str = None, password: str = None, host: str = None, port: str = None):
        self.conn = psycopg2.connect(dbname=dbname, user=username, password=password, host=host, port=port)
        self.curr = self.conn.cursor()

    def __del__(self):
        self.curr.close()
        self.conn.close()


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