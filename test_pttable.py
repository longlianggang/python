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
    for i in range(2,74):
        diff.append(date[i]-date_old[i])
         
        if diff[i-2]<0:
            diff_sign.append('↓')
        elif diff[i-2]>0:
            diff_sign.append('↑')
        else:
            diff_sign.append(' ')
    th=["注册人数",      
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
     "牛牛税收",	  
     "牛牛系统输赢",   
     "牛牛人数",	   
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
     "注充比例",	
     "注绑比例",	
     "绑充比例"]	
    
    
    text=[]
    text.append('''%s 数据\n -------------------------\n  %9s今日  与昨日对比\n'''%(report_time,""))
    for i in range(2,61):
        if isinstance(date[i],(int)):
            text.append("%-10s%d    %d %s \n"%(th[i-2],date[i],diff[i-2],diff_sign[i-2]))
        else:
            if (i==37):
                hang="%-10s%.4f%% %.4f%% %s \n"%(th[i-2],date[i]*100,diff[i-2]*100,diff_sign[i-2])
                text.append(hang)
            elif (i==42):
                hang="%-10s%.4f%% %.4f%% %s \n"%(th[i-2],date[i]*100,diff[i-2]*100,diff_sign[i-2])
                text.append(hang)	  
            else:
                hang="%-10s%.2f %.2f %s \n"%(th[i-2],date[i],diff[i-2],diff_sign[i-2])
                text.append(hang)
        
	
    for i in range(61,74):
        hang="%-10s%.4f%%   %.4f%% %s \n"%(th[i-2],date[i]*100,diff[i-2]*100,diff_sign[i-2])
        text.append(hang)
    text.append('''-------------------------\n 统计时间 %s'''%(date[1]))
    txt="".join(text)
    #print (txt)

    #print("循环发送开始")
    #chatid=[382877244,210414429]
    #sendmessage(txt,382877244)
    #for i in chatid:
    #   print (i)
    sendmessage(txt,i)
            
    #print("发送完毕")                               
if __name__ == '__main__':
     print_table()

													
										
