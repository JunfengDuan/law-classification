import pymysql


class PDBC:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self, charset='utf8'):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               db=self.db, charset=charset)
        return conn

    def query(self, sql):
        with self.cursor as cur:
            cur.execute(sql)
            records = cur.fetchall()
        return records

    def save(self, sql, args):
        with self.cursor as cur:
            cur.executemany(sql, args)
            self.conn.commit()


pdbc = PDBC(host="192.168.130.236", port=3306, user="root", password="root", db="flfgk")
