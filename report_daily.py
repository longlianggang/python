#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cx_Oracle
import os
import datetime
import time
import urllib.request
import urllib
import sys



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


     
        
        
        
if __name__ == '__main__':
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
			 
     print (diff[69])   
     print (diff[70])
     txt='''%s  数据
------------------------------------
                 今日      与昨日对比
                                  
 注册人数      %d     %d   %s            
 注册绑定人数  %d     %d   %s            
 登录绑定用户数 %d    %d   %s            
 登录人数        %d      %d  %s          
 IOS登录总数     %d      %d  %s          
 安卓登录总数   %d      %d   %s          
 新进入IP      %d      %d    %s          
 充值总数    %.2f    %.2f  %s            
 新用户充值  %.2f    %.2f   %s           
 老用户充值  %.2f    %.2f   %s           
 官方充值    %d   %d   %s                
 新用户官方充值	 %d    %d   %s           
 老用户官方充值	 %d    %d   %s           
 代理充值        %d    %d   %s           
 新用户代理充值	 %d    %d   %s           
 老用户代理充值	 %d    %d   %s           
 充值人数        %d    %d   %s           
 新用户充值人数	 %d    %d   %s           
 老用户充值人数	 %d    %d   %s           
 在线充值人数	 %d    %d   %s           
 新用户在线充值人数  %d   %d %s          
 老用户在线充值人数  %d   %d %s          
 代理充值人数	     %d   %d %s          
 新用户代理充值人数  %d   %d %s          
 老用户代理充值人数  %d   %d %s          
 充值笔数       %d   %d   %s             
 充值成功笔数	%d   %d   %s             
 充值失败笔数	%d   %d   %s             
 在线充值笔数	%d   %d   %s             
 在线充值成功笔数  %d    %d %s           
 在线充值失败笔数  %d    %d %s           
 代理充值笔数	 %d  %d  %s              
 代理充值成功笔数   %d  %d  %s           
 代理充值失败笔数   %d  %d  %s           
 人均充值（ARPPU)   %.2f    %.2f  %s     
 付费率	     %.4f%%    %.4f%%  %s        
 人均贡献（ARPU)   %.2f  %.2f %s         
 兑换		 %d     %d   %s              
 兑换人数	 %d     %d   %s              
 活跃人数	 %d     %d   %s              
 营收比		%.2f%%    %.2f%%    %s       
 营收		%d      %d  %s               
 代理进货	%d     %d   %s               
 斗地主税收	%.2f   %.2f  %s              
 斗地主系统输赢	  %.2f  %.2f  %s         
 斗地主人数	  %d    %d    %s             
 炸金花税收	  %.2f  %.2f  %s             
 炸金花系统输赢	  %.2f  %.2f  %s         
 炸金花人数	  %d     %d    %s            
 百人牛牛税收	  %d     %d    %s        
 百人牛牛系统输赢   %.2f    %.2f   %s    
 百人牛牛人数	   %d      %d     %s     
 龙虎斗税收	   %.2f   %.2f   %s          
 龙虎斗系统输赢	   %d     %d     %s      
 龙虎斗人数	   %d     %d     %s          
 捕鱼税收	   %.2f   %.2f   %s          
 捕鱼系统输赢	   %.2f   %.2f   %s      
 捕鱼人数	   %d     %d     %s          
 总税收		   %d     %d     %s          
 昨日留存	   %.4f%%   %.4f%%   %s      
 二日留存	   %.4f%%   %.4f%%   %s      
 三日留存	   %.4f%%   %.4f%%   %s      
 四日留存	   %.4f%%   %.4f%%   %s      
 五日留存	   %.4f%%   %.4f%%   %s      
 六日留存	   %.4f%%   %.4f%%   %s      
 七日留存	   %.4f%%   %.4f%%   %s      
 八日留存	   %.2f%%   %.4f%%   %s      
 九日留存	   %.4f%%   %.4f%%   %s      
 十日留存	   %.4f%%   %.4f%%   %s      
 今日注充比例	%.4f%%   %.4f%%  %s      
 今日注绑比例	%.4f%%   %.4f%%  %s      
 今日绑充比例	%.4f%%   %.4f%%  %s      
---------------------------------
 统计时间：%s
                                    ''' %(  report_time,
											date[2],diff[0],diff_sign[0],  
                                            date[3],diff[1],diff_sign[1],
                                            date[4],diff[2],diff_sign[2],
                                            date[5],diff[3],diff_sign[3],
                                            date[6],diff[4],diff_sign[4],
                                            date[7],diff[5],diff_sign[5],
                                            date[8],diff[6],diff_sign[6],
                                            date[9],diff[7],diff_sign[7],
                                            date[10],diff[8],diff_sign[8],
                                            date[11],diff[9],diff_sign[9],
                                            date[12],diff[10],diff_sign[10],
                                            date[13],diff[11],diff_sign[11],
                                            date[14],diff[12],diff_sign[12],
                                            date[15],diff[13],diff_sign[13],
                                            date[16],diff[14],diff_sign[14],
                                            date[17],diff[15],diff_sign[15],
                                            date[18],diff[16],diff_sign[16],
                                            date[19],diff[17],diff_sign[17],
                                            date[20],diff[18],diff_sign[18],
                                            date[21],diff[19],diff_sign[19],
                                            date[22],diff[20],diff_sign[20],
                                            date[23],diff[21],diff_sign[21],
                                            date[24],diff[22],diff_sign[22],
                                            date[25],diff[23],diff_sign[23],
                                            date[26],diff[24],diff_sign[24],
                                            date[27],diff[25],diff_sign[25],
                                            date[28],diff[26],diff_sign[26],
                                            date[29],diff[27],diff_sign[27],
                                            date[30],diff[28],diff_sign[28],
                                            date[31],diff[29],diff_sign[29],
                                            date[32],diff[30],diff_sign[30],
                                            date[33],diff[31],diff_sign[31],
                                            date[34],diff[32],diff_sign[32],
                                            date[35],diff[33],diff_sign[33],
                                            date[36],diff[34],diff_sign[34],
                                            date[37]*100,diff[35],diff_sign[35],
                                            date[38],diff[36],diff_sign[36],
                                            date[39],diff[37],diff_sign[37],
                                            date[40],diff[38],diff_sign[38],
                                            date[41],diff[39],diff_sign[39],
                                            date[42]*100,diff[40],diff_sign[40],
                                            date[43],diff[41],diff_sign[41],
                                            date[44],diff[42],diff_sign[42],
                                            date[45],diff[43],diff_sign[43],
                                            date[46],diff[44],diff_sign[44],
                                            date[47],diff[45],diff_sign[45],
                                            date[48],diff[46],diff_sign[46],
                                            date[49],diff[47],diff_sign[47],
                                            date[50],diff[48],diff_sign[48],
                                            date[51],diff[49],diff_sign[49],
                                            date[52],diff[50],diff_sign[50],
                                            date[53],diff[51],diff_sign[51],
                                            date[54],diff[52],diff_sign[52],
                                            date[55],diff[53],diff_sign[53],
                                            date[56],diff[54],diff_sign[54],
                                            date[57],diff[55],diff_sign[55],
                                            date[58],diff[56],diff_sign[56],
                                            date[59],diff[57],diff_sign[57],
                                            date[60],diff[58],diff_sign[58],
                                            date[61]*100,diff[59],diff_sign[59],
                                            date[62]*100,diff[60],diff_sign[60],
                                            date[63]*100,diff[61],diff_sign[61],
                                            date[64]*100,diff[62],diff_sign[62],
                                            date[65]*100,diff[63],diff_sign[63],
                                            date[66]*100,diff[64],diff_sign[64],
                                            date[67]*100,diff[65],diff_sign[65],
                                            date[68]*100,diff[66],diff_sign[66],
                                            date[69]*100,diff[67],diff_sign[67],
                                            date[70]*100,diff[68],diff_sign[68],
                                            date[71]*100,diff[69],diff_sign[69],
					    date[72]*100,diff[70],diff_sign[70],
					    date[73]*100,diff[71],diff_sign[71],
                                            date[1])

     print("循环发送开始")

     #chatid=[382877244,210414429]
     chatid=[382877244]
     
     for i in chatid:
         print (i)
         sendmessage(txt,i)
            
     print("发送完毕")
													
										
