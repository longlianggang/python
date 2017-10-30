# -*- coding: utf-8 -*-   
import os
import re
import codecs




filepath=r"D:\work\auto_script\config_web"





def __replace(f1):
#替换开关
    for i in range (len(f1)):
        match_switch=re.search(r'debug_number number1',f1[i])
        if match_switch:
            #print (i)
            #print (f1[i])
            f1[i]=f1[i].replace("0.01f","0")

    #替换登录域名
    url="\"http://loginus.jiujiu66.com/jiujiu/login.php\""
    for i in range(len(f1)):
        match_login=re.search(r'appstore itmsforssl',f1[i])
        match_version=re.search(r'/V',f1[i])
        if match_login:
            f1[i]=re.sub("\".*?\"",url,f1[i])
            
        if match_version:
            url="\"http://login.jiujiu66.com/jiujiu/login.php\""
    return f1
           
def channel_id(filepath):
    channel_files=[x for x in os.listdir(filepath) if os.path.isfile(os.path.join(filepath,x))]
    for i in range(len(channel_files)):
        channel_num=re.sub("\D","",channel_files[i])
        if not os.path.isdir(os.path.join(filepath,channel_num)):
            os.mkdir(os.path.join(filepath,channel_num))
        f=codecs.open(r'D:\work\auto_script\config_web\config_%d.xml'%(int(channel_num)),'r+','utf-8')
        f1=f.readlines()
        __replace(f1)
        channelfile=os.path.join(filepath,channel_num,'config.xml')
        f2=codecs.open(channelfile,'w','utf-8')
        f2.writelines(f1)
        f2.close
            



if __name__ == '__main__':
    
    channel_id(filepath)


 
