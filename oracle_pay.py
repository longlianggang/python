#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cx_Oracle
import os
import datetime
import time
import urllib.request
import urllib
import socket 

wx_sql="select max(pay_time) from  zyy_user.pay2_order_record where pay_instance_id in (161,41,4)  and  pay_time>sysdate-1 order by pay_time desc"
ali_sql="select max(pay_time) from  zyy_user.pay2_order_record where pay_instance_id not in (161,41,4,1)  and  pay_time>sysdate-1 order by pay_time desc "
token='400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg'


def pay_time(sql):
 
    conn=cx_Oracle.connect('zabbix/zabbix@43.243.72.66/ora11g')
    c=conn.cursor()
    x=c.execute(sql)
    date=x.fetchall()
    #end_time={'wx':'','ali':''}
    #end_time['wx'] =str(date_wx[0][0])
    #end_time['ali']=str(date_ali[0][0])
    #print ("Number of rows returned: %d" % x.rowcount  )
    
    c.close()
    
    conn.close()
    time1=time.mktime(date[0][0].timetuple())
    return time1

def diff(sql):
    time1=pay_time(sql)
    time2=time.time()
    diff_time=int(time2)-int(time1)

    return  diff_time


def sendmessage(txt):
    url='https://api.telegram.org/bot400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg/sendmessage?chat_id=-222547519&text=%s'%(txt) 
    print (txt)

    req=urllib.request.Request(url)

    print (req)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    print (res)


def alert_wx():
        
    wx_time=300
    t1=diff(wx_sql)
    t_min=t1/60
    try:
        if t1>wx_time:
            txt="已有%d分钟未完成微信充值" %(t_min)
            txt=urllib.parse.quote(txt)
            sendmessage(txt)
            print ("已有%d分钟未完成微信充值" %(t_min))
        else:
            print("微信充值OK")
    except socket.error as e:
        print("error")
      
       
        
def alert_ali():
    ali_time=120
    t2=diff(ali_sql)
    t_min=t2/60
    try:
            
        if  t2>ali_time:
            txt1="已有%d分钟未完成支付宝充值"%(t_min)
            txt1=urllib.parse.quote(txt1)
            sendmessage(txt1)
            print ("已有%d分钟未完成支付宝充值"%(t_min))
        
        else:
            txt1=urllib.parse.quote("支付宝充值正常")
            #sendmessage(txt1)
            print(txt1)
            print ("支付宝充值OK")
    except os.error as e:
        print("error")
        
        
        
if __name__ == '__main__':
    
    

    while True:
        try:
            alert_wx()
            alert_ali()
            time.sleep(5)
        except socket.error as e:
            print("error")
            break
