#!/usr/bin/env python
import time 
import datetime 

def str_2_time(timein:str)->time :
    if(timein.count(':') == 1):
        mystr = timein + ':00'
    else:
        mystr = timein
    date_time_obj = datetime.datetime.strptime(mystr, '%H:%M:00')
    return date_time_obj.time()

#a = str_2_time('11:22:00')
#print('time a: ',a,' as ',str(a))
#c = str_2_time('11:25')
#print(c < a)
