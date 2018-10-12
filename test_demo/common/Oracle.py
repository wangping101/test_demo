# coding:utf-8
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
u'''Oracle数据库相关操作
连接数据库名称如：xxx
查询一组数据：oracle_getrows
查询某个字段对应的字符串：oracle_getstring
执行sql语句：oracle_sql
关闭oracle连接：oracle_close
'''

dbname = {"user": "czth_sales",
          "pwd": "123456",
          "dsn": "192.168.0.136:1521/ORCL136"}


class OracleUtil():
    def __init__(self):
        ''' 连接池方式'''
        self.db_info = dbname
        self.conn = OracleUtil.__getConnect(self.db_info)

    @staticmethod
    def __getConnect(db_info):
        ''' 静态方法，从连接池中取出连接'''
        try:
            con = cx_Oracle.connect(db_info['user'], db_info['pwd'], db_info['dsn'])
            return con
        except Exception as a:
            print("数据库连接异常：%s" % a)

    def oracle_getrows(self, sql):
        ''' 执行查询sql'''
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows
            except Exception as a:
                print("执行sql出现异常：%s" % a)
            finally:
                cursor.close()
        except Exception as a:
            print("数据库连接异常：%s" % a)

    def oracle_getstring(self, sql):
        ''' 查询某个字段的对应值'''
        rows = self.oracle_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def oracle_sql(self, sql):
        ''' 执行sql语句'''
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)

            except Exception as a:
                print("执行sql出现异常：%s" % a)
            finally:
                cursor.close()
        except Exception as a:
            print("数据库连接异常：%s" % a)

    def orcle_close(self):
        ''' 关闭orcle连接'''

        try:
            self.conn.close()
        except Exception as a:
            print("数据库关闭时异常：%s" % a)


if __name__ == "__main__":
    oracl = OracleUtil()

    sql = "select t.user_id,t.union_id  from th_user_info t where t.union_id is not null "

    r = oracl.oracle_getrows(sql)
    # print(r)
    # r2 = json.dumps(r, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
    # print(r2)
    # oracl.orcle_close()
    r1 = ['user_id', 'union_id']
    for i in r:
        s = dict(zip(r1, i))
        print(s)
