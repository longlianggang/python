#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cx_Oracle
import os
import datetime
import time
import urllib.request
import urllib





sql="select decode(type,1,'银行卡提现',0,'支付宝提现'),sum(mcoin) from zyy_user.prize_mrecord  where trunc(update_time)=trunc(sysdate-1)  and status=2  group by type"
token='400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg'



def prize_mrecord(sql):
 
    conn=cx_Oracle.connect('zabbix/zabbix@43.243.72.66/ora11g')
    c=conn.cursor()
    x=c.execute(sql)
    date=x.fetchall()
    
    print (date)
    
    
    #print ("Number of rows returned: %d" % x.rowcount  )
    
    c.close()
    
    conn.close()
    #time1=time.mktime(date[0][0].timetuple())
    return date

    


def sendmessage(txt,chatid):

    
    txt=urllib.parse.quote(txt)
         
    url="https://api.telegram.org/bot400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg/sendmessage?chat_id=%s&text=%s"%(chatid,txt)

   

    req=urllib.request.Request(url)

   
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    print (res)


     
        
        
        
if __name__ == '__main__':
     report_time=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")
     date=prize_mrecord(sql)

     txt='''%s 提现汇报，老板请查收：
-----------------------------------
               %s
               %s
                '''%(report_time,date[0],date[1])

     
     sendmessage(txt,358721823)

     
 									
										
