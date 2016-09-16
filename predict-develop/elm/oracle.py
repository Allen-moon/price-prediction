#!/usr/bin/python
#encoding=utf-8
import sys
import cx_Oracle
#import export.oracle_config as config
#import oracle_config as config
import config

class Oracle:
    __con = None
    __cur = None

    def __init__( self, host   = config.oralce_db_host,   \
                        user   = config.oralce_db_user,   \
                        passwd = config.oralce_db_password, \
                        listener     = config.oralce_listener_name,  \
                        port   = config.oralce_db_port):
        try:
            connect_str = (user+'/'+passwd+'@'+host+':'+'%d'+'/'+listener)%port
            print(connect_str)
            self.__con=cx_Oracle.connect(connect_str)
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
            return self.__cur
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False

    #return 表结构
    def table_colsname( self, sql ):
        print ('SQL [%s]' % sql)
        col_list = []
        try:
            self.__cur.execute(sql)
            for col in self.__cur.description:
                col_list.append(col[0])
            print(col_list)
            return col_list
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return []



if __name__ == '__main__':
    sql_conn = Oracle()
    
