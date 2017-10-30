# -*- coding: utf-8 -*-   
import os
import re

sourced=r"D:\work\auto_script\enable"
targetd=r"D:\work\auto_script"
ml=[x for x in os.listdir('.') if os.path.isdir(x)]

value = re.compile(r'^[-+]?[0-9]+$')

for i in range(len(ml)):
    
    print (ml[i])
    result = value.match(ml[i])
    print (result)
    if result:
         for f in os.listdir(sourced):
             sourcef = os.path.join(sourced, f)
             targetf = os.path.join(targetd,ml[i],"patch_diff_dwc",f)
             os.system ("copy %s %s" % (sourcef, targetf))
             
    else:
        print("不是目标目录")
            



 
