from random import choice
import string
import pymysql


# class wrap mysql operations
class mysql_init(object):
    def __init__(self,conn):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="guyueyu710520",
            db="test",
            charset="utf8"
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except :
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


#  main process
def process():
    dbconn = mysql_init(None)
    conn = dbconn.cursor()
    dropTable(conn)
    createTable(conn)
    insertData(conn)
    dbconn.commit()
    rows=queryData(conn)
    print(rows)
    dbconn.close()


def dropTable(conn):
    conn.execute("drop table if exists test")


def createTable(conn):
    sql_create = """create table test (`key` varchar(50) not null)"""
    conn.execute(sql_create)


def insertData(conn):
    insert_sql = "insert into test values(%(value)s)"
    key_list = getAllKey(keyLength,keyNum)
    conn.executemany(insert_sql,[dict(value=v) for v in key_list])


def queryData(conn):
    sql = "select * from test"
    conn.execute(sql)
    rows = conn.fetchall()
    return rows


keyNum = 200
keyLength = 20
# wrapper ???
def printKey(func):
    def _printKey(length,num):
        for i in func(length,num):
            print(i)
    return _printKey

# get nums key
def getAllKey(length,num,result=None):
    if result is None:
        result = set()
    while len(result)<num:
        if getKey(length) in result:
            continue
        else:
            result.add(getKey(length))
    return result

# get one key
def getKey(length):
    baseChar = string.ascii_letters + string.digits
    keyList = [choice(baseChar) for _ in range(length)]
    return ''.join(keyList)

process()