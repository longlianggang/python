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


sql="select * from zyy_user.report_daily where trunc(create_time)=trunc(sysdate)"
sql_old="select * from zyy_user.report_daily where trunc(create_time)=trunc(sysdate-1)"

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
    date_old=report_daily(sql_old)
    diff=[]
    diff_sign=[]
    for i in range(2,75):
        diff.append(date[i]-date_old[i])
         
        if diff[i-2]<0:
            diff_sign.append('↓')
        elif diff[i-2]>0:
            diff_sign.append('↑')
        else:
            diff_sign.append(' ')
    th=["最高在线",
        "注册人数",      
     "注册绑定人数", 
     "登录绑定用户数", 
     "登录人数",       
     "IOS登录总数",     
     "安卓登录总数",   
     "新进入IP",      
     "充值总数",   
     "新用户充值",  
     "老用户充值",  
     "官方充值",   
     "新用户官方充值",	 
     "老用户官方充值",	 
     "代理充值",          
     "新用户代理充值",	
     "老用户代理充值",	 
     "充值人数",          
     "新用户充值人数",	
     "老用户充值人数",	  
     "在线充值人数",	 
     "新用户在线充值人数 ", 
     "老用户在线充值人数",  
     "代理充值人数",	     
     "新用户代理充值人数", 
     "老用户代理充值人数",  
     "充值笔数",              
     "充值成功笔数",	       
     "充值失败笔数",	     
     "在线充值笔数",	    
     "在线充值成功笔数",      
     "在线充值失败笔数",   
     "代理充值笔数",	     
     "代理充值成功笔数",       
     "代理充值失败笔数",      
     "人均充值（ARPPU)",  
     "付费率",	     
     "人均贡献（ARPU)",    
     "兑换",		     
     "兑换人数",	        
     "活跃人数",	        
     "营收比",		
     "营收",		   
     "代理进货",	        
     "斗地主税收",	
     "斗地主系统输赢",	 
     "斗地主人数",	   
     "炸金花税收",	    
     "炸金花系统输赢",	 
     "炸金花人数",	  
     "百人牛牛税收",	  
     "百人牛牛系统输赢",   
     "百人牛牛人数",	   
     "龙虎斗税收",	  
     "龙虎斗系统输赢",	   
     "龙虎斗人数",	  
     "捕鱼税收",	  
     "捕鱼系统输赢",	  
     "捕鱼人数",	   
     "总税收",		   
     "昨日留存",	   
     "二日留存",	   
     "三日留存",	   
     "四日留存",	   
     "五日留存",	   
     "六日留存",	   
     "七日留存",	   
     "八日留存",	   
     "九日留存",	   
     "十日留存",	   
     "今日注充比例",	
     "今日注绑比例",	
     "今日绑充比例"]	
    
    text=PrettyTable(["项目", "今日", "与昨日对比", ""])
    text.align["项目"]="1"
    text.padding_width = 1
    for i in range(2,62):
        if isinstance(date[i],(int)):
            text.add_row([th[i-2],date[i],diff[i-2],diff_sign[i-2]])
        else:
            if (i==38):		  	  
                text.add_row([th[i-2],"%.4f%%"%(date[i]*100),"%.4f%%"%(diff[i-2]*100),diff_sign[i-2]])
            elif (i==43):
                text.add_row([th[i-2],"%.4f%%"%(date[i]*100),"%.4f%%"%(diff[i-2]*100),diff_sign[i-2]])		  
            else:
                text.add_row([th[i-2],"%.2f"%(date[i]),"%.2f"%(diff[i-2]),diff_sign[i-2]])
            
	
    for i in range(62,75):
        text.add_row([th[i-2],"%.4f%%"%(date[i]*100),"%.4f%%"%(diff[i-2]*100),diff_sign[i-2]])
    print (str(text))
    text=str(text)
    sendmessage(text,382877244)
                                    
if __name__ == '__main__':
     print_table()

     #print("循环发送开始")

     #chatid=[382877244,210414429]
     #chatid=[382877244]
     
     #for i in chatid:
      #   print (i)
      #   sendmessage(txt,i)
            
     #print("发送完毕")
													
										
