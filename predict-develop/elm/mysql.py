#!/usr/bin/python
#encoding=utf-8
import sys
import pymysql
import config

class MySQL:
    __con = None
    __cur = None

    def __init__( self, host   = config.db_host,   \
                        user   = config.db_user,   \
                        passwd = config.db_password, \
                        db     = config.db_name):
        try:
            self.__con=pymysql.connect( host=host, user=user, \
                                        passwd=passwd, db=db, \
                                        charset='utf8')
        except Exception:
            sys.stderr.write( 'Failed to connect Databse\n')
            return

        self.__cur = self.__con.cursor()


    def __del__( self ):
        if self.__cur:
            self.__cur.close()
        if self.__con:
            self.__con.close()

    # return True if execute ok, False if error occurs
    def execute( self, sql ):
        print ('SQL [%s]' % sql)
        try:
            self.__cur.execute(sql)
            self.__con.commit()
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False
        return True

    # get last auto-increment id if insert
    def getLastId( self ):
        return self.__cur.lastrowid

    # return result if execute ok, False if error occurs
    def select( self, sql ):
        print ('SQL [%s]' % sql)
        try:
            self.__cur.execute(sql)
            return self.__cur.fetchall()
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False
    
    def select_params( self, sql ,varlist):
        print ('SQL [%s]' % sql)
        try:
            self.__cur.execute(sql,varlist)
            return self.__cur.fetchall()
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False

    def execute_params(self, sql,varlist):
        print ('SQL [%s]' % sql)
        try:
            self.__cur.execute(sql,varlist)
            self.__con.commit()
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False
        return True

    def get_col_names(self, sql):
        print('SQL [%s]' % sql)
        try:
            self.__cur.execute(sql)
            columns=[col[0] for col in self.__cur.description]
            return columns
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False


import openpyxl
if __name__ == '__main__':
    sql_conn = MySQL()
