from  random  import randrange
from  select import dict_2_str
from  schedule import ScheduledRides

class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_stops: list):
        self.__bus_schedule :  {ScheduledRides} = {}
        self.destination: str = destination
        self.line_number: int = line_number
        self.list_stops: list = list_stops
        self.origin: str = origin


    def __str__(self) -> str:
        st = dict_2_str(self.get_as_dict(True),0)
        return st
       
    def display_r(self):
        print_dict(self.get_as_dict(True),0)


    def update_route(self, line_num, origin=None, destination=None, list_stops=None):
        pass

    def add_schedule(self, origin_time:int, destination_time:int, driver_name:str):
        s:ScheduledRides = ScheduledRides(origin_time, destination_time, driver_name)
        id:int = int(randrange(1,1000))
        self.__bus_schedule[id] = s
        
    def get_as_dict(self,with_driver_name:bool):
        medic = {}
        medic['origin'] =  self.origin
        medic['destination'] =  self.destination
        medic['stops'] = self.list_stops
        for s in self.__bus_schedule:
            medic['sceudle: '+str(s)] = self.__bus_schedule[s].get_as_dict(with_driver_name)
        return medic
        
# a = BusRoute(5,'telaviv', 'ramm', ['aaa','bbb'])
# print(a)