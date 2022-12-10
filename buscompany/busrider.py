import pickle
import time 
import datetime 
busriderdict ={}

class ScheduleRide:

    def __init__(self,origin_time:time,dest_time:time,driver_name: str,stops:list):
        self.__origin_time = origin_time
        self.__dest_time = dest_time
        self.__driver_name = driver_name
        self.__stops = stops

#date_time_str = '2022-12-01 10:27:03.929149'
# strptime(input_string, input_format)
date_time_obj = datetime.datetime.strptime('0:27', '%H:%M')
print(date_time_obj,date_time_obj.time())
a = date_time_obj.time()
print(type(a))
exit()
#sr1 = ScheduleRide(
print(busriderdict)
with open('busrider.pickle', 'wb') as handle:
    pickle.dump(busriderdict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('busrider.pickle', 'rb') as handle:
    busriderdict2 = pickle.load(handle)
print(busriderdict2)