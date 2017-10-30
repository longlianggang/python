#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cx_Oracle
import os
import datetime
import time
import urllib.request
import urllib
import socket
import codecs
import pymysql.connections
import pymysql
import logging  
import logging.config  
logging.config.fileConfig("logging.conf")    
logger = logging.getLogger("main")


sql="select pay_instance_id,sum(plan_pay) from zyy_user.pay2_order_record where  order_status=1 and trunc(create_time)=trunc(sysdate)  group by pay_instance_id"
sql_select='select pay_instance_id,money_limit,pay_desc from pay_limit where status=1'
token='400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg'


def get_data(sql):

    try:
        conn=cx_Oracle.connect('zabbix/zabbix@103.80.26.199/ora11g')
        c=conn.cursor()
        x=c.execute(sql)
        date=x.fetchall()
    except cx_Oracle.DatabaseError as msg: 
        logger.error(msg)
    
    
    c.close()
    conn.close()
    return date

def mysql_select(sql):
    
        try:
            conn = pymysql.connect(host='47.90.101.26', port=3306, user='root', passwd='A123456',db='admin',charset='utf8')
            cur = conn.cursor()
            cur.execute(sql)
            date=cur.fetchall()
        except Exception as e:
            logger.error(e)
        cur.close()
        conn.close()
        return date
        
def mysql_connect(sql):
    
    config={'host':'47.90.101.26',#默认127.0.0.1
        'user':'root',
        'password':'A123456',
        'port':3306 ,#默认即为3306
        'database':'admin',
        'charset':'utf8'#默认即为utf8
        }
    try:
        conn=pymysql.connections.Connection(**config)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        logger.error(msg)
    cur.close()
    conn.close()   

def sendmessage(txt):

    
    #txt="%s今日充值已超过阀值，目前充值数额为%d"%(merchant,pay)
    txt=urllib.parse.quote(txt)

    url='https://api.telegram.org/bot400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg/sendmessage?chat_id=382877244&text=%s'%(txt) 
    
    req=urllib.request.Request(url)
    

    res_data = urllib.request.urlopen(req)
    res = res_data.read()
   

       


def get_limit():

    
    txt=[]

    w1=codecs.open('num.txt', 'r+','utf-8')
        
    lines=w1.readlines()
        
    for line in lines:
        
        if not line.startswith('#'):
            
            txt.append(line.replace("\n","").split(","))
        

    
    return txt
    
def alert_limit():
    txt=mysql_select(sql_select)
    date=get_data(sql)
    if txt:
        logger.debug('current pay_limit is %s'%(txt))
    else:
        logger.debug('目前充值没有限制')
    for  i in range(len(txt)):

        for j in range(len(date)):
            #print (int(txt[i][0]))
            #print (type(date[j][0]))
            if int(txt[i][0])==date[j][0]:
                diff=date[j][1]-int(txt[i][1])
                print (diff)
                if diff>0:
                    logger.debug('%s current pay is %d'%(txt[i][2],date[j][1]))
                    sql_update='update pay_limit set status=0 where pay_instance_id=%d'%(txt[i][0])        
                    #mysql_connect(sql_update)
                    text="%s今日充值已超过阀值，目前充值数额为%d"%(txt[i][2],date[j][1])
                    sendmessage(text) 
                    logger.debug('开始循环检测')
                    time.sleep(60)
                    count=1
                    while True:
                        
                        logger.debug('等待2分钟………')
                        time.sleep(120)
                        date=get_data(sql)
                        instance_num=get_data("select count(*) from zyy_user.config_channel_pay2 where pay_instance_id=%d"%(txt[i][1]))
                        if instance_num:
                            if count<3:
                                text="%s目前充值数额为%d,咋还不切换支付呢"%(txt[i][2],date[j][1])
                                logger.debug(text)
                                sendmessage(text)
                                count=count+1
                                
                                
                            else:
                                text="还不切换，只能帮你到这了"
                                sendmessage(text)
                                break
                            continue 
                                
                        else:
                            text="支付已切换，报警关闭"
                            sendmessage(text)
                            break

                else:
                   logger.debug("%s目前充值数额为%d"%(txt[i][2],date[j][1]))
            
                      
    
    

        
        
if __name__ == '__main__':
    
    while True:
        alert_limit()
        time.sleep(5)    
