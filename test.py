# -*- coding: utf-8 -*-   
import os
import re



def group_float(n, sep = ','):
    
    
    t=str("%.2f"%(n)).split('.')
    s = str(abs(int(t[0])))[::-1]
    
    groups = []
    i = 0
    while i < len(s):
        groups.append(s[i:i+4])
        i+=4
    
    retval = sep.join(groups)[::-1]
    result = retval+'.'+t[1]
    if n < 0:
        return '-%s' % retval
    else:
        return result
    
def group_int(n, sep = ','):
    s = str(abs(n))[::-1]
    groups = []
    i = 0
    while i < len(s):
        groups.append(s[i:i+4])
        i+=4
    retval = sep.join(groups)[::-1]
    if n < 0:
        return '-%s' % retval
    else:
        return retval

def get_(n):
    if  isinstance(n,int):
        return group_int(n)
    else:
        return group_float(n)
         
    #print ("b is %s"%(b))
     

if __name__ == '__main__':
    b=get_(10000.544546501212)
    print (b)
   
    



     
