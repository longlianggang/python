# -*- coding: utf-8 -*-   
import os
import re
import shutil
sourced=r"D:\work\auto_script\m1"
targetd_1=r"D:\work\auto_script"
ml=[x for x in os.listdir('.') if os.path.isdir(x)]
print (os.listdir('.'))
value = re.compile(r'^[-+]?[0-9]+$')

for i in range(len(ml)):
    
    print (ml[i])
    print (result)
    if i>1:
         
        targetd = os.path.join(targetd,ml[i])
        os.system ("copy %s %s" % (sourcef, targetf))
             
    else:
        print("不是目标目录")
            



 
