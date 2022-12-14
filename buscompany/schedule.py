from datetime import datetime


class ScheduledRides:
    def __init__(self, origin_time:int, destination_time:int, driver_name:str):
        self.__origin_time = origin_time
        self.__destination_time = destination_time
        self.__driver_name = driver_name
        self.__delays:list = []

    def __str__(self):
        return dict_2_str(self.get_as_dict(True))


    def get_as_dict(self,withdriver:bool)->dict:
        scheddict = {}
        scheddict['origin_time'] = self.__origin_time
        scheddict['destination_time'] = self.__destination_time
        if withdriver:
            scheddict['driver_name'] = self.__driver_name
        scheddict['delays'] = self.__delays
        return scheddict
        
    def add_delay(self,adelay):
        self.__delays.append(adelay)
        
        
