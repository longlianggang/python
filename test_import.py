# -*- coding: utf-8 -*-   
import test

    

if __name__ == '__main__':
    a=123456.154
    if  isinstance(a,int):
        b=test.group_int(a)
    else:
        b=test.group_float(a)
    print ("b is %s"%(b))
   
    



     
