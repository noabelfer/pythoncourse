from datetime import datetime


class ScheduledRides:
    def __init__(self, origin_time:int, destination_time:int, driver_name:str):
        self.__origin_time = origin_time
        self.__destination_time = destination_time
        self.__driver_name = driver_name
        self.__delays:list = []

    def __str__(self):
        st = "origin: "+str(self.__origin_time) + " destination: " + str(self.__destination_time) + " driver: " + \
        self.__driver_name
        st += "\n     delays: "
        if len(self.__delays) == 0:
            st+= ' None'
            return st
        for i in self.__delays:
            st += ' '+str(i)
        return st

    def get_as_dict(self,withdriver:bool):
        scheddict = {}
        scheddict['origin_time'] = self.__origin_time
        scheddict['destination_time'] = self.__destination_time
        if withdriver:
            scheddict['driver_name'] = self.__driver_name
        scheddict['delays'] = self.__delays
        return scheddict
        
        
        
