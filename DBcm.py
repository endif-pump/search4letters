import pymysql

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.con = pymysql.connect(**self.configuration)
        self.cur = self.con.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.con.commit()
        self.cur.close()
        self.con.close()
