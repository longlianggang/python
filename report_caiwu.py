#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cx_Oracle
import os
import datetime
import time
import urllib.request
import urllib
import sys
from prettytable  import PrettyTable


sql="select brnn_tax,lhd_tax,zjh_tax,fish_tax,ddz_tax,register_count,active_player,prize_count,pay_count,brnn_win_lost+lhd_win_lost from zyy_user.report_daily where trunc(create_time)=trunc(sysdate)"
sql1="select sum(coin)  from (select prize_ticket * 2147483647/1000 + game_coin/1000 - game_prop_1 * 2147483647/1000 - match_ticket/1000 coin, t.*, t.rowid from zyy_user.GAME_TASK_LOG t where task_id = 107019 and server_id in (10711,10712,10713) and game_coin!=0 and  trunc(create_time)=trunc(sysdate-1)    order by create_time desc) where rownum<4"
sql2="select sum(coin)  from (select prize_ticket * 2147483647/1000 + game_coin/1000 - game_prop_1 * 2147483647/1000 - match_ticket/1000 coin, t.*, t.rowid from zyy_user.GAME_TASK_LOG t where task_id = 107019 and server_id in (10721) and game_coin!=0 and  trunc(create_time)=trunc(sysdate-1)    order by create_time desc) where rownum<2"
sql3="select sum(coin)  from (select prize_ticket * 2147483647/1000 + game_coin/1000 - game_prop_1 * 2147483647/1000 - match_ticket/1000 coin, t.*, t.rowid from zyy_user.GAME_TASK_LOG t where task_id = 107019 and server_id =10731 and game_coin!=0 and  trunc(create_time)=trunc(sysdate-1)    order by create_time desc) where rownum<2"
sql4="select sum(coin)  from (select prize_ticket * 2147483647/1000 + game_coin/1000 - game_prop_1 * 2147483647/1000 - match_ticket/1000 coin, t.*, t.rowid from zyy_user.GAME_TASK_LOG t where task_id = 107019 and server_id =10741 and game_coin!=0 and  trunc(create_time)=trunc(sysdate-1)    order by create_time desc) where rownum<2"
token='400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg'



def report_daily(sql):
 
    conn=cx_Oracle.connect('zabbix/zabbix@103.80.26.199/ora11g')
    c=conn.cursor()
    x=c.execute(sql)
    date=x.fetchall()
   
    #end_time={'wx':'','ali':''}
    #end_time['wx'] =str(date_wx[0][0])
    #end_time['ali']=str(date_ali[0][0])
    #print ("Number of rows returned: %d" % x.rowcount  )
    
    c.close()
    
    conn.close()
    #time1=time.mktime(date[0][0].timetuple())
    return date[0]

  


def sendmessage(txt,chatid):
    
    
    txt=urllib.parse.quote(txt)
         
    url="https://api.telegram.org/bot400170734:AAFhlyglk28-GbtYBBY3ogn4sS3CiRvnKHg/sendmessage?chat_id=%s&text=%s"%(chatid,txt)
	
   
    #print(url)
    req=urllib.request.Request(url)

    print (req)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    #print (res)

def print_table():
    report_time=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    date=report_daily(sql)
    date1=report_daily(sql1)
    date2=report_daily(sql2)
    date3=report_daily(sql3)
    date4=report_daily(sql4)
    
    th=["牛牛玩家抽水",
        "龙虎玩家抽水",      
     "诈金花玩家抽水", 
     "捕鱼玩家抽水", 
     "斗地主玩家抽水",
     "注册总数",
     "活跃人数",     
     "提现人数去重",   
     "充值人数去重",      
     "机器人输赢",   	   
     "10元场",	   
     "1元场",	   
     "0.1元场抽水",	
     "0.01元场抽水"	
             ]	
    
    text=[]
    text.append('''项目：菠菜电玩城\n %s\n统计数据\n'''%(report_time))
    
    for i in range(len(date)):
        if isinstance(date[i],(int)):
            text.append("%s:%d \n"%(th[i],date[i]))
        else:
             
            text.append("%s:%.2f \n"%(th[i],date[i]))
            
    text.append('''\n捕鱼抽水：\n --------------\n''')
    text.append("%s:%.2f \n"%(th[10],date4[0]))
    text.append("%s:%.2f \n"%(th[11],date3[0]))
    text.append("%s:%.2f \n"%(th[12],date2[0]))
    text.append("%s:%.2f \n"%(th[13],date1[0]))            
    
    txt="".join(text)
    sendmessage(txt,-280327193)
    #sendmessage(txt,382877244)                               
if __name__ == '__main__':
     print_table()

     #print("循环发送开始")

     #chatid=[382877244,210414429]
     #chatid=[382877244]
     
     #for i in chatid:
      #   print (i)
      #   sendmessage(txt,i)
            
     #print("发送完毕")
													
										
