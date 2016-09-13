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

    def execute_params( self, sql,varlist):
        print ('SQL [%s]' % sql)
        try:
            self.__cur.execute(sql,varlist)
            self.__con.commit()
        except Exception:
            sys.stderr.write( 'Failed to execute SQL[%s]\n' % sql )
            return False
        return True

def write_file_2_mysql(sql_conn,row_elses):
    sql='INSERT INTO CPI(CPI_date,CPI_zhi,CPI_zhange,CPI_zhangfu) values(%s,%s,%s,%s)'
    sql_conn.execute_params(sql,row_elses)
'''
CPI_date date,
CPI_zhi varchar(10),
CPI_zhange varchar(10),
CPI_zhangfu varchar(10)

xgxjtzs_date date,
xgxjtzs_zhi varchar(10),
xgxjtzs_zhange varchar(10),
xgxjtzs_zhangfu varchar(10)

'''

if __name__ == '__main__':

    date_init ='2016-03-15'
    sql_conn = MySQL()

    # sql=' SELECT * FROM jkk_qingdao_final  WHERE jkk_date > "2013-12-31" and jkk_date < "2016-02-01"'
    sql=' SELECT * FROM jkk_qingdao_final  WHERE jkk_date > "2013-12-31" and jkk_date < "2016-02-01"'
    date_init_1 = sql_conn.select(sql)
    print(date_init_1)
    for each_day in date_init_1:
        date_init = each_day[1]
        print(date_init)

        #before
        #before
        #before
        #before
        #before
        #before_1mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 30 and TO_DAYS("%s") - TO_DAYS(jkk_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
            # print(price_1)
            # sum1 = sum1 + each[3]
        before_1mon = sum1/before_mon_len
        fore_1mon = round(before_1mon, 2)
        print(fore_1mon)

        

         #before_2mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 60 and TO_DAYS("%s") - TO_DAYS(jkk_date) > 30' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        before_2mon = sum1/before_mon_len
        before_2mon = round(before_2mon, 2)
        print(before_2mon)

        #before_3mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 90 and TO_DAYS("%s") - TO_DAYS(jkk_date) > 60' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        before_3mon = sum1/before_mon_len
        before_3mon = round(before_3mon, 2)
        print(before_3mon)

            #before_4mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 120 and TO_DAYS("%s") - TO_DAYS(jkk_date) > 90' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        before_4mon = sum1/before_mon_len
        before_4mon = round(before_4mon, 2)
        print(before_4mon)

            #before_5mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 150 and TO_DAYS("%s") - TO_DAYS(jkk_date) > 120' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        before_5mon = sum1/before_mon_len
        before_5mon = round(before_5mon, 2)
        print(before_5mon)

            #before_6mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 180 and TO_DAYS("%s") - TO_DAYS(jkk_date) > 150' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        before_6mon = sum1/before_mon_len
        before_6mon = round(before_6mon, 2)
        print(before_6mon)

        
        #after_1mon
        #after
        #after
        #after
        #after
        #after
        #after
        # sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS("%s") - TO_DAYS(jkk_date) <= 0 and TO_DAYS("%s") - TO_DAYS(jkk_date) >= -30' %(date_init,date_init)
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS(jkk_date) - TO_DAYS("%s") <= 30 and TO_DAYS(jkk_date) - TO_DAYS("%s") > 0' %(date_init,date_init)
        after_mon_price=sql_conn.select(sql)
        # print(after_mon_price)
        # print(len(before_1mon_price))
        after_mon_len = len(after_mon_price)
        sum1=0
        for each in after_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        after_1mon = sum1/after_mon_len
        after_1mon = round(after_1mon, 2)
        print(after_1mon)

         #after_1mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS(jkk_date) - TO_DAYS("%s") <= 60 and TO_DAYS(jkk_date) - TO_DAYS("%s") > 30' %(date_init,date_init)
        after_mon_price=sql_conn.select(sql)
        # print(after_mon_price)
        # print(len(before_1mon_price))
        after_mon_len = len(after_mon_price)
        sum1=0
        for each in after_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        after_2mon = sum1/after_mon_len
        after_2mon = round(after_2mon, 2)
        print(after_2mon)

        #after_3mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS(jkk_date) - TO_DAYS("%s") <= 90 and TO_DAYS(jkk_date) - TO_DAYS("%s") > 60' %(date_init,date_init)
        after_mon_price=sql_conn.select(sql)
        # print(after_mon_price)
        # print(len(before_1mon_price))
        after_mon_len = len(after_mon_price)
        sum1=0
        for each in after_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        after_3mon = sum1/after_mon_len
        after_3mon = round(after_3mon, 2)
        print(after_3mon)     

        #after_4mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS(jkk_date) - TO_DAYS("%s") <= 120 and TO_DAYS(jkk_date) - TO_DAYS("%s") > 90' %(date_init,date_init)
        after_mon_price=sql_conn.select(sql)
        # print(after_mon_price)
        # print(len(before_1mon_price))
        after_mon_len = len(after_mon_price)
        sum1=0
        for each in after_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        after_4mon = sum1/after_mon_len
        after_4mon = round(after_4mon, 2)
        print(after_4mon)      


        #after_5mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS(jkk_date) - TO_DAYS("%s") <= 150 and TO_DAYS(jkk_date) - TO_DAYS("%s") > 120' %(date_init,date_init)
        after_mon_price=sql_conn.select(sql)
        # print(after_mon_price)
        # print(len(before_1mon_price))
        after_mon_len = len(after_mon_price)
        sum1=0
        for each in after_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        after_5mon = sum1/after_mon_len
        after_5mon = round(after_5mon, 2)
        print(after_5mon)  


        #after_6mon
        sql=' SELECT * FROM jkk_qingdao_final  WHERE TO_DAYS(jkk_date) - TO_DAYS("%s") <= 180 and TO_DAYS(jkk_date) - TO_DAYS("%s") > 150' %(date_init,date_init)
        after_mon_price=sql_conn.select(sql)
        # print(after_mon_price)
        # print(len(before_1mon_price))
        after_mon_len = len(after_mon_price)
        sum1=0
        for each in after_mon_price:
            flag = each[3].index("-")
            price = (int(each[3][0:flag])+int(each[3][(flag+1):]))/2
            sum1 = sum1 +price
        after_6mon = sum1/after_mon_len
        after_6mon = round(after_6mon, 2)
        print(after_6mon)  


        # fore_meiyuan
        # fore_meiyuan
        # fore_meiyuan
        # fore_meiyuan
        # fore_meiyuan
        # fore_meiyuan_1
        sql=' SELECT * FROM meiyuan  WHERE TO_DAYS("%s") - TO_DAYS(meiyuan_date) <= 30 and TO_DAYS("%s") - TO_DAYS(meiyuan_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_meiyuan_1 = round(before_1mon, 2)
        print(fore_meiyuan_1)


        #before_2mon
        sql=' SELECT * FROM meiyuan  WHERE TO_DAYS("%s") - TO_DAYS(meiyuan_date) <= 60 and TO_DAYS("%s") - TO_DAYS(meiyuan_date) > 30' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_meiyuan_2 = round(before_1mon, 2)
        print(fore_meiyuan_2)

        #before_3mon
        sql=' SELECT * FROM meiyuan  WHERE TO_DAYS("%s") - TO_DAYS(meiyuan_date) <= 90 and TO_DAYS("%s") - TO_DAYS(meiyuan_date) > 60' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_meiyuan_3 = round(before_1mon, 2)
        print(fore_meiyuan_3)

        #before_4mon
        sql=' SELECT * FROM meiyuan  WHERE TO_DAYS("%s") - TO_DAYS(meiyuan_date) <= 120 and TO_DAYS("%s") - TO_DAYS(meiyuan_date) > 90' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_meiyuan_4 = round(before_1mon, 2)
        print(fore_meiyuan_4)

        #before_5mon
        sql=' SELECT * FROM meiyuan  WHERE TO_DAYS("%s") - TO_DAYS(meiyuan_date) <= 150 and TO_DAYS("%s") - TO_DAYS(meiyuan_date) > 120' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_meiyuan_5 = round(before_1mon, 2)
        print(fore_meiyuan_5)

        #before_6mon
        sql=' SELECT * FROM meiyuan  WHERE TO_DAYS("%s") - TO_DAYS(meiyuan_date) <= 180 and TO_DAYS("%s") - TO_DAYS(meiyuan_date) > 150' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_meiyuan_6 = round(before_1mon, 2)
        print(fore_meiyuan_6)






        # fore_psjgzs
        # fore_psjgzs
        # fore_psjgzs
        # fore_psjgzs
        # fore_psjgzs
        # fore_psjgzs_1
        sql=' SELECT * FROM psjgzs  WHERE TO_DAYS("%s") - TO_DAYS(psjgzs_date) <= 30 and TO_DAYS("%s") - TO_DAYS(psjgzs_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_psjgzs_1 = round(before_1mon, 2)
        print(fore_psjgzs_1)


        #before_2mon
        sql=' SELECT * FROM psjgzs  WHERE TO_DAYS("%s") - TO_DAYS(psjgzs_date) <= 60 and TO_DAYS("%s") - TO_DAYS(psjgzs_date) > 30' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_psjgzs_2 = round(before_1mon, 2)
        print(fore_psjgzs_2)

        #before_3mon
        sql=' SELECT * FROM psjgzs  WHERE TO_DAYS("%s") - TO_DAYS(psjgzs_date) <= 90 and TO_DAYS("%s") - TO_DAYS(psjgzs_date) > 60' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_psjgzs_3 = round(before_1mon, 2)
        print(fore_psjgzs_3)

        #before_4mon
        sql=' SELECT * FROM psjgzs  WHERE TO_DAYS("%s") - TO_DAYS(psjgzs_date) <= 120 and TO_DAYS("%s") - TO_DAYS(psjgzs_date) > 90' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_psjgzs_4 = round(before_1mon, 2)
        print(fore_psjgzs_4)

        #before_5mon
        sql=' SELECT * FROM psjgzs  WHERE TO_DAYS("%s") - TO_DAYS(psjgzs_date) <= 150 and TO_DAYS("%s") - TO_DAYS(psjgzs_date) > 120' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_psjgzs_5 = round(before_1mon, 2)
        print(fore_psjgzs_5)

        #before_6mon
        sql=' SELECT * FROM psjgzs  WHERE TO_DAYS("%s") - TO_DAYS(psjgzs_date) <= 180 and TO_DAYS("%s") - TO_DAYS(psjgzs_date) > 150' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_psjgzs_6 = round(before_1mon, 2)
        print(fore_psjgzs_6)




        # fore_haiyun
        # fore_haiyun
        # fore_haiyun
        # fore_haiyun
        # fore_haiyun
        # fore_haiyun_1mon
        sql=' SELECT * FROM haiyun  WHERE TO_DAYS("%s") - TO_DAYS(haiyun_date) <= 30 and TO_DAYS("%s") - TO_DAYS(haiyun_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_mon_price))
        flag1 = 0
        flag2 = 0
        flag3 = 0
        sum1=0
        sum2=0
        sum3=0
        for each in before_mon_price:
            if each[2] == '-':
                flag1=flag1+1
            else:
                sum1 = sum1 + float(each[2])
            if each[3] == '-':
                flag2=flag2+1
            else:   
                sum2 = sum2 + float(each[3])
            if each[4] == '-':
                flag3=flag3+1
            else:                  
                sum3 = sum3 + float(each[4])
        before_mon_len_1 = len(before_mon_price)-flag1
        before_mon_len_2 = len(before_mon_price)-flag2
        before_mon_len_3 = len(before_mon_price)-flag3

        before_1mon = sum1/before_mon_len_1
        fore_haiyunBDI_1 = round(before_1mon, 2)
        before_1mon = sum2/before_mon_len_2
        fore_haiyunBCI_1 = round(before_1mon, 2)
        before_1mon = sum3/before_mon_len_3
        fore_haiyunBDTI_1 = round(before_1mon, 2)
        print(fore_haiyunBDI_1,fore_haiyunBCI_1,fore_haiyunBDTI_1)


        #before_2mon
        sql=' SELECT * FROM haiyun  WHERE TO_DAYS("%s") - TO_DAYS(haiyun_date) <= 60 and TO_DAYS("%s") - TO_DAYS(haiyun_date) > 30' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_mon_price))
        flag1 = 0
        flag2 = 0
        flag3 = 0
        sum1=0
        sum2=0
        sum3=0
        for each in before_mon_price:
            if each[2] == '-':
                flag1=flag1+1
            else:
                sum1 = sum1 + float(each[2])
            if each[3] == '-':
                flag2=flag2+1
            else:   
                sum2 = sum2 + float(each[3])
            if each[4] == '-':
                flag3=flag3+1
            else:                  
                sum3 = sum3 + float(each[4])
        before_mon_len_1 = len(before_mon_price)-flag1
        before_mon_len_2 = len(before_mon_price)-flag2
        before_mon_len_3 = len(before_mon_price)-flag3

        before_1mon = sum1/before_mon_len_1
        fore_haiyunBDI_2 = round(before_1mon, 2)
        before_1mon = sum2/before_mon_len_2
        fore_haiyunBCI_2 = round(before_1mon, 2)
        before_1mon = sum3/before_mon_len_3
        fore_haiyunBDTI_2 = round(before_1mon, 2)
        print(fore_haiyunBDI_2,fore_haiyunBCI_2,fore_haiyunBDTI_2)

        #before_3mon
        sql=' SELECT * FROM haiyun  WHERE TO_DAYS("%s") - TO_DAYS(haiyun_date) <= 90 and TO_DAYS("%s") - TO_DAYS(haiyun_date) > 60' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_mon_price))
        flag1 = 0
        flag2 = 0
        flag3 = 0
        sum1=0
        sum2=0
        sum3=0
        for each in before_mon_price:
            if each[2] == '-':
                flag1=flag1+1
            else:
                sum1 = sum1 + float(each[2])
            if each[3] == '-':
                flag2=flag2+1
            else:   
                sum2 = sum2 + float(each[3])
            if each[4] == '-':
                flag3=flag3+1
            else:                  
                sum3 = sum3 + float(each[4])
        before_mon_len_1 = len(before_mon_price)-flag1
        before_mon_len_2 = len(before_mon_price)-flag2
        before_mon_len_3 = len(before_mon_price)-flag3

        before_1mon = sum1/before_mon_len_1
        fore_haiyunBDI_3 = round(before_1mon, 2)
        before_1mon = sum2/before_mon_len_2
        fore_haiyunBCI_3 = round(before_1mon, 2)
        before_1mon = sum3/before_mon_len_3
        fore_haiyunBDTI_3 = round(before_1mon, 2)
        print(fore_haiyunBDI_3,fore_haiyunBCI_3,fore_haiyunBDTI_3)

        #before_4mon
        sql=' SELECT * FROM haiyun  WHERE TO_DAYS("%s") - TO_DAYS(haiyun_date) <= 120 and TO_DAYS("%s") - TO_DAYS(haiyun_date) > 90' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_mon_price))
        flag1 = 0
        flag2 = 0
        flag3 = 0
        sum1=0
        sum2=0
        sum3=0
        for each in before_mon_price:
            if each[2] == '-':
                flag1=flag1+1
            else:
                sum1 = sum1 + float(each[2])
            if each[3] == '-':
                flag2=flag2+1
            else:   
                sum2 = sum2 + float(each[3])
            if each[4] == '-':
                flag3=flag3+1
            else:                  
                sum3 = sum3 + float(each[4])
        before_mon_len_1 = len(before_mon_price)-flag1
        before_mon_len_2 = len(before_mon_price)-flag2
        before_mon_len_3 = len(before_mon_price)-flag3

        before_1mon = sum1/before_mon_len_1
        fore_haiyunBDI_4 = round(before_1mon, 2)
        before_1mon = sum2/before_mon_len_2
        fore_haiyunBCI_4 = round(before_1mon, 2)
        before_1mon = sum3/before_mon_len_3
        fore_haiyunBDTI_4 = round(before_1mon, 2)
        print(fore_haiyunBDI_4,fore_haiyunBCI_4,fore_haiyunBDTI_4)

        #before_5mon
        sql=' SELECT * FROM haiyun  WHERE TO_DAYS("%s") - TO_DAYS(haiyun_date) <= 150 and TO_DAYS("%s") - TO_DAYS(haiyun_date) > 120' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_mon_price))
        flag1 = 0
        flag2 = 0
        flag3 = 0
        sum1=0
        sum2=0
        sum3=0
        for each in before_mon_price:
            if each[2] == '-':
                flag1=flag1+1
            else:
                sum1 = sum1 + float(each[2])
            if each[3] == '-':
                flag2=flag2+1
            else:   
                sum2 = sum2 + float(each[3])
            if each[4] == '-':
                flag3=flag3+1
            else:                  
                sum3 = sum3 + float(each[4])
        before_mon_len_1 = len(before_mon_price)-flag1
        before_mon_len_2 = len(before_mon_price)-flag2
        before_mon_len_3 = len(before_mon_price)-flag3

        before_1mon = sum1/before_mon_len_1
        fore_haiyunBDI_5 = round(before_1mon, 2)
        before_1mon = sum2/before_mon_len_2
        fore_haiyunBCI_5 = round(before_1mon, 2)
        before_1mon = sum3/before_mon_len_3
        fore_haiyunBDTI_5 = round(before_1mon, 2)
        print(fore_haiyunBDI_5,fore_haiyunBCI_5,fore_haiyunBDTI_5)

        #before_6mon
        sql=' SELECT * FROM haiyun  WHERE TO_DAYS("%s") - TO_DAYS(haiyun_date) <= 180 and TO_DAYS("%s") - TO_DAYS(haiyun_date) > 150' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_mon_price))
        flag1 = 0
        flag2 = 0
        flag3 = 0
        sum1=0
        sum2=0
        sum3=0
        for each in before_mon_price:
            if each[2] == '-':
                flag1=flag1+1
            else:
                sum1 = sum1 + float(each[2])
            if each[3] == '-':
                flag2=flag2+1
            else:   
                sum2 = sum2 + float(each[3])
            if each[4] == '-':
                flag3=flag3+1
            else:                  
                sum3 = sum3 + float(each[4])
        before_mon_len_1 = len(before_mon_price)-flag1
        before_mon_len_2 = len(before_mon_price)-flag2
        before_mon_len_3 = len(before_mon_price)-flag3

        before_1mon = sum1/before_mon_len_1
        fore_haiyunBDI_6 = round(before_1mon, 2)
        before_1mon = sum2/before_mon_len_2
        fore_haiyunBCI_6 = round(before_1mon, 2)
        before_1mon = sum3/before_mon_len_3
        fore_haiyunBDTI_6 = round(before_1mon, 2)
        print(fore_haiyunBDI_6,fore_haiyunBCI_6,fore_haiyunBDTI_6)


        # fore_WTI
        # fore_WTI
        # fore_WTI
        # fore_WTI
        # fore_WTI
        # fore_WTI_1mon
        sql=' SELECT * FROM WTI  WHERE TO_DAYS("%s") - TO_DAYS(WTI_date) <= 30 and TO_DAYS("%s") - TO_DAYS(WTI_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        flag = 0   
        sum1=0
        for each in before_mon_price:
            if each[2] == '-':
                flag=flag+1
            else:
                sum1 = sum1 + float(each[2])
        before_1mon = sum1/(before_mon_len-flag)
        fore_WTI_1 = round(before_1mon, 2)
        print(fore_WTI_1)


        #before_2mon
        sql=' SELECT * FROM WTI  WHERE TO_DAYS("%s") - TO_DAYS(WTI_date) <= 60 and TO_DAYS("%s") - TO_DAYS(WTI_date) > 30' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        flag = 0   
        sum1=0
        for each in before_mon_price:
            if each[2] == '-':
                flag=flag+1
            else:
                sum1 = sum1 + float(each[2])
        before_1mon = sum1/(before_mon_len-flag)
        fore_WTI_2 = round(before_1mon, 2)
        print(fore_WTI_2)

        #before_3mon
        sql=' SELECT * FROM WTI  WHERE TO_DAYS("%s") - TO_DAYS(WTI_date) <= 90 and TO_DAYS("%s") - TO_DAYS(WTI_date) > 60' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        flag = 0   
        sum1=0
        for each in before_mon_price:
            if each[2] == '-':
                flag=flag+1
            else:
                sum1 = sum1 + float(each[2])
        before_1mon = sum1/(before_mon_len-flag)
        fore_WTI_3 = round(before_1mon, 2)
        print(fore_WTI_3)

        #before_4mon
        sql=' SELECT * FROM WTI  WHERE TO_DAYS("%s") - TO_DAYS(WTI_date) <= 120 and TO_DAYS("%s") - TO_DAYS(WTI_date) > 90' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        flag = 0   
        sum1=0
        for each in before_mon_price:
            if each[2] == '-':
                flag=flag+1
            else:
                sum1 = sum1 + float(each[2])
        before_1mon = sum1/(before_mon_len-flag)
        fore_WTI_4 = round(before_1mon, 2)
        print(fore_WTI_4)

        #before_5mon
        sql=' SELECT * FROM WTI  WHERE TO_DAYS("%s") - TO_DAYS(WTI_date) <= 150 and TO_DAYS("%s") - TO_DAYS(WTI_date) > 120' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        flag = 0   
        sum1=0
        for each in before_mon_price:
            if each[2] == '-':
                flag=flag+1
            else:
                sum1 = sum1 + float(each[2])
        before_1mon = sum1/(before_mon_len-flag)
        fore_WTI_5 = round(before_1mon, 2)
        print(fore_WTI_5)

        #before_6mon
        sql=' SELECT * FROM WTI  WHERE TO_DAYS("%s") - TO_DAYS(WTI_date) <= 180 and TO_DAYS("%s") - TO_DAYS(WTI_date) > 150' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        flag = 0   
        sum1=0
        for each in before_mon_price:
            if each[2] == '-':
                flag=flag+1
            else:
                sum1 = sum1 + float(each[2])
        before_1mon = sum1/(before_mon_len-flag)
        fore_WTI_6 = round(before_1mon, 2)
        print(fore_WTI_6)





        # fore_PMI
        # fore_PMI
        # fore_PMI
        # fore_PMI
        # fore_PMI
        # fore_PMI_1mon
        sql=' SELECT * FROM PMI  WHERE TO_DAYS("%s") - TO_DAYS(PMI_date) <= 31 and TO_DAYS("%s") - TO_DAYS(PMI_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_PMI_1 = round(before_1mon, 2)
        print(fore_PMI_1)


        #before_2mon
        sql=' SELECT * FROM PMI  WHERE TO_DAYS("%s") - TO_DAYS(PMI_date) <= 62 and TO_DAYS("%s") - TO_DAYS(PMI_date) > 31' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_PMI_2 = round(before_1mon, 2)
        print(fore_PMI_2)

        #before_3mon
        sql=' SELECT * FROM PMI  WHERE TO_DAYS("%s") - TO_DAYS(PMI_date) <= 93 and TO_DAYS("%s") - TO_DAYS(PMI_date) > 62' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_PMI_3 = round(before_1mon, 2)
        print(fore_PMI_3)

        #before_4mon
        sql=' SELECT * FROM PMI  WHERE TO_DAYS("%s") - TO_DAYS(PMI_date) <= 124 and TO_DAYS("%s") - TO_DAYS(PMI_date) > 93' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_PMI_4 = round(before_1mon, 2)
        print(fore_PMI_4)

        #before_5mon
        sql=' SELECT * FROM PMI  WHERE TO_DAYS("%s") - TO_DAYS(PMI_date) <= 155 and TO_DAYS("%s") - TO_DAYS(PMI_date) > 124' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_PMI_5 = round(before_1mon, 2)
        print(fore_PMI_5)

        #before_6mon
        sql=' SELECT * FROM PMI  WHERE TO_DAYS("%s") - TO_DAYS(PMI_date) <= 186 and TO_DAYS("%s") - TO_DAYS(PMI_date) > 155' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_PMI_6 = round(before_1mon, 2)
        print(fore_PMI_6)


        # fore_tksjkl
        # fore_tksjkl
        # fore_tksjkl
        # fore_tksjkl
        # fore_tksjkl
        # fore_tksjkl_1mon
        sql=' SELECT * FROM tksjkl  WHERE TO_DAYS("%s") - TO_DAYS(tksjkl_date) <= 31 and TO_DAYS("%s") - TO_DAYS(tksjkl_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksjkl_1 = round(before_1mon, 2)
        print(fore_tksjkl_1)


        #before_2mon
        sql=' SELECT * FROM tksjkl  WHERE TO_DAYS("%s") - TO_DAYS(tksjkl_date) <= 62 and TO_DAYS("%s") - TO_DAYS(tksjkl_date) > 31' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksjkl_2 = round(before_1mon, 2)
        print(fore_tksjkl_2)

        #before_3mon
        sql=' SELECT * FROM tksjkl  WHERE TO_DAYS("%s") - TO_DAYS(tksjkl_date) <= 93 and TO_DAYS("%s") - TO_DAYS(tksjkl_date) > 62' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksjkl_3 = round(before_1mon, 2)
        print(fore_tksjkl_3)

        #before_4mon
        sql=' SELECT * FROM tksjkl  WHERE TO_DAYS("%s") - TO_DAYS(tksjkl_date) <= 124 and TO_DAYS("%s") - TO_DAYS(tksjkl_date) > 93' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksjkl_4 = round(before_1mon, 2)
        print(fore_tksjkl_4)

        #before_5mon
        sql=' SELECT * FROM tksjkl  WHERE TO_DAYS("%s") - TO_DAYS(tksjkl_date) <= 155 and TO_DAYS("%s") - TO_DAYS(tksjkl_date) > 124' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksjkl_5 = round(before_1mon, 2)
        print(fore_tksjkl_5)

        #before_6mon
        sql=' SELECT * FROM tksjkl  WHERE TO_DAYS("%s") - TO_DAYS(tksjkl_date) <= 186 and TO_DAYS("%s") - TO_DAYS(tksjkl_date) > 155' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksjkl_6 = round(before_1mon, 2)
        print(fore_tksjkl_6)



        # fore_tksykcl
        # fore_tksykcl
        # fore_tksykcl
        # fore_tksykcl
        # fore_tksykcl
        # fore_tksykcl_1mon
        sql=' SELECT * FROM tksykcl  WHERE TO_DAYS("%s") - TO_DAYS(tksykcl_date) <= 31 and TO_DAYS("%s") - TO_DAYS(tksykcl_date) > 0' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksykcl_1 = round(before_1mon, 2)
        print(fore_tksykcl_1)


        #before_2mon
        sql=' SELECT * FROM tksykcl  WHERE TO_DAYS("%s") - TO_DAYS(tksykcl_date) <= 62 and TO_DAYS("%s") - TO_DAYS(tksykcl_date) > 31' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksykcl_2 = round(before_1mon, 2)
        print(fore_tksykcl_2)

        #before_3mon
        sql=' SELECT * FROM tksykcl  WHERE TO_DAYS("%s") - TO_DAYS(tksykcl_date) <= 93 and TO_DAYS("%s") - TO_DAYS(tksykcl_date) > 62' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksykcl_3 = round(before_1mon, 2)
        print(fore_tksykcl_3)

        #before_4mon
        sql=' SELECT * FROM tksykcl  WHERE TO_DAYS("%s") - TO_DAYS(tksykcl_date) <= 124 and TO_DAYS("%s") - TO_DAYS(tksykcl_date) > 93' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksykcl_4 = round(before_1mon, 2)
        print(fore_tksykcl_4)

        #before_5mon
        sql=' SELECT * FROM tksykcl  WHERE TO_DAYS("%s") - TO_DAYS(tksykcl_date) <= 155 and TO_DAYS("%s") - TO_DAYS(tksykcl_date) > 124' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksykcl_5 = round(before_1mon, 2)
        print(fore_tksykcl_5)

        #before_6mon
        sql=' SELECT * FROM tksykcl  WHERE TO_DAYS("%s") - TO_DAYS(tksykcl_date) <= 186 and TO_DAYS("%s") - TO_DAYS(tksykcl_date) > 155' %(date_init,date_init)
        before_mon_price=sql_conn.select(sql)
        # print(before_mon_price)
        # print(len(before_1mon_price))
        before_mon_len = len(before_mon_price)
        sum1=0
        for each in before_mon_price:
            sum1 = sum1 + float(each[2])
        before_1mon = sum1/before_mon_len
        fore_tksykcl_6 = round(before_1mon, 2)
        print(fore_tksykcl_6)

        date_init = str(date_init)
        print(type(date_init))
        date_init = date_init[0:4] + date_init[5:7] + date_init[8:10]


        # sql='INSERT INTO PB(PB_date,date_init,meiyuan_price,psjgzs_price,haiyun_BDI_price,haiyun_BCI_price,haiyun_BDTI_price,WTI_price,PMI_zhizao_price,tksjkl_jkl,tksykcl_zhi,gangtie_cugang) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' %(PB_price,date_init,meiyuan_price,psjgzs_price,haiyun_BDI_price,haiyun_BCI_price,haiyun_BDTI_price,WTI_price,PMI_zhizao_price,tksjkl_jkl,tksykcl_zhi,gangtie_cugang)
        sql='INSERT INTO PB(PB_date,after_1mon,after_2mon,after_3mon,after_4mon,after_5mon,after_6mon,before_1mon,before_2mon,before_3mon,before_4mon,before_5mon,before_6mon,fore_meiyuan_1,fore_meiyuan_2,fore_meiyuan_3,fore_meiyuan_4,fore_meiyuan_5,fore_meiyuan_6,fore_psjgzs_1,fore_psjgzs_2,fore_psjgzs_3,fore_psjgzs_4,fore_psjgzs_5,fore_psjgzs_6,fore_haiyunBDI_1,fore_haiyunBDI_2,fore_haiyunBDI_3,fore_haiyunBDI_4,fore_haiyunBDI_5,fore_haiyunBDI_6,fore_haiyunBCI_1,fore_haiyunBCI_2,fore_haiyunBCI_3,fore_haiyunBCI_4,fore_haiyunBCI_5,fore_haiyunBCI_6,fore_haiyunBDTI_1,fore_haiyunBDTI_2,fore_haiyunBDTI_3,fore_haiyunBDTI_4,fore_haiyunBDTI_5,fore_haiyunBDTI_6,fore_WTI_1,fore_WTI_2,fore_WTI_3,fore_WTI_4,fore_WTI_5,fore_WTI_6,fore_PMI_1,fore_PMI_2,fore_PMI_3,fore_PMI_4,fore_PMI_5,fore_PMI_6,fore_tksjkl_1,fore_tksjkl_2,fore_tksjkl_3,fore_tksjkl_4,fore_tksjkl_5,fore_tksjkl_6,fore_tksykcl_1,fore_tksykcl_2,fore_tksykcl_3,fore_tksykcl_4,fore_tksykcl_5,fore_tksykcl_6) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' %(date_init,after_1mon,after_2mon,after_3mon,after_4mon,after_5mon,after_6mon,fore_1mon,before_2mon,before_3mon,before_4mon,before_5mon,before_6mon,fore_meiyuan_1,fore_meiyuan_2,fore_meiyuan_3,fore_meiyuan_4,fore_meiyuan_5,fore_meiyuan_6,fore_psjgzs_1,fore_psjgzs_2,fore_psjgzs_3,fore_psjgzs_4,fore_psjgzs_5,fore_psjgzs_6,fore_haiyunBDI_1,fore_haiyunBDI_2,fore_haiyunBDI_3,fore_haiyunBDI_4,fore_haiyunBDI_5,fore_haiyunBDI_6,fore_haiyunBCI_1,fore_haiyunBCI_2,fore_haiyunBCI_3,fore_haiyunBCI_4,fore_haiyunBCI_5,fore_haiyunBCI_6,fore_haiyunBDTI_1,fore_haiyunBDTI_2,fore_haiyunBDTI_3,fore_haiyunBDTI_4,fore_haiyunBDTI_5,fore_haiyunBDTI_6,fore_WTI_1,fore_WTI_2,fore_WTI_3,fore_WTI_4,fore_WTI_5,fore_WTI_6,fore_PMI_1,fore_PMI_2,fore_PMI_3,fore_PMI_4,fore_PMI_5,fore_PMI_6,fore_tksjkl_1,fore_tksjkl_2,fore_tksjkl_3,fore_tksjkl_4,fore_tksjkl_5,fore_tksjkl_6,fore_tksykcl_1,fore_tksykcl_2,fore_tksykcl_3,fore_tksykcl_4,fore_tksykcl_5,fore_tksykcl_6)

        # -sql='INSERT INTO test_PB(PB_price) values(%s)' %(PB_price)
        sql_conn.execute(sql)


        # print(type(date_init))

    # data_rows=[]
    # with open("cpi.txt") as f:
    #     row=f.readline()
    #     while row:
    #         print(row)
    #         row_elses=row.split(' ')
    #         for i in range(len(row_elses)):
    #             if(row_elses[i]!=None):
    #                 row_elses[i]=row_elses[i].strip("\t").strip('\n').strip(' ')
    #         print(row_elses)
    #         write_file_2_mysql(sql_conn,row_elses)
    #         row=f.readline()
