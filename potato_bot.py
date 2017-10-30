#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cx_Oracle
import os
import datetime
import time
import urllib.request
import urllib
import sys
import json
#from prettytable  import PrettyTable
import test


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

    


def sendmessage(chattype,txt,chatid):
    
    
    #txt=urllib.parse.quote(txt)
         
    url="https://bot.potato.im:5423/8026668:Nlr1XaN8bIR1vzymJQHq322y/sendTextMessage"
        
    headers = { 
        'Content-Type':'application/json'
       
		 }   
    postdata={"chat_type":chattype,"chat_id":chatid,"text":txt}
    postdata=bytes(json.dumps(postdata),'utf8')
    req=urllib.request.Request(url=url, headers=headers, data=postdata)
    
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    #print (res)

def print_table():
    report_time=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    date=report_daily(sql)
    date_old=report_daily(sql_old)
    rjgx=(date[61]+date[53]+date[56])/date[42]
    rjgx_old=(date_old[61]+date_old[53]+date_old[56])/date_old[42]
    diff_rjgx=rjgx-rjgx_old
    if diff_rjgx<0:
        diff_rjgx_sign='↓'
    elif diff_rjgx>0:
        diff_rjgx_sign='↑'
    else:
        diff_rjgx_sign=' '
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
     "ARPU",    
     "兑换",                 
     "兑换人数",                
     "活跃人数",                
     "营收比",
     "营收",               
     "代理进货",                
     "斗地主税收",
     "斗地主系统输赢",   
     "斗地主最高在线",         
     "炸金花税收",          
     "炸金花系统输赢",   
     "炸金花最高在线",        
     "牛牛税收",          
     "牛牛系统输赢",   
     "牛牛最高在线",           
     "龙虎斗税收",        
     "龙虎斗系统输赢",     
     "龙虎斗最高在线",        
     "捕鱼税收",          
     "捕鱼系统输赢",      
     "捕鱼最高在线",           
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
    text.append('''项目：永盛科技一部-BCDWC\n %s\n今日与昨日对比\n'''%(report_time))
    for i in range(2,62):
        if isinstance(date[i],(int)):
            text.append("%s：%s  %s%s \n"%(th[i-2],test.get_(date[i]),test.get_(diff[i-2]),diff_sign[i-2]))
        else:
            if (i==38):
                hang="%s：%.4f%%  %.4f%%%s \n"%(th[i-2],date[i]*100,diff[i-2]*100,diff_sign[i-2])
                text.append(hang)
                text.append("人均贡献:%.2f  %.2f%s\n"%(rjgx,diff_rjgx,diff_rjgx_sign))
            elif (i==43):
                hang="%s：%.4f%%  %.4f%%%s \n"%(th[i-2],date[i]*100,diff[i-2]*100,diff_sign[i-2])
                text.append(hang)         
            else:
                hang="%s：%s  %s%s \n"%(th[i-2],test.get_(date[i]),test.get_(diff[i-2]),diff_sign[i-2])
                text.append(hang)
        

    for i in range(62,75):
        hang="%s：%.4f%%  %.4f%%%s \n"%(th[i-2],date[i]*100,diff[i-2]*100,diff_sign[i-2])
        text.append(hang)
    text.append('''-------------------------\n 统计时间 %s'''%(date[1]))
    txt="".join(text)
    print (txt)

    print("循环发送开始")
    chatid=[382877244,210414429,414541349]
    sendmessage(3,txt,3361)
    #sendmessage(1,txt,8003075)
    #for i in chatid:
       #print (i)
       #sendmessage(txt,i)
            
    print("发送完毕")                               
if __name__ == '__main__':
    print_table()
