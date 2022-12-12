from typing import Type
from busroute import BusRoute


class BestBusCompany:

    def __init__(self):
        self.__bus_route: {BusRoute} = {}
        
    def line_used(self,line:int)->bool:
        return line in self.__bus_route
    
    def get_busriute(self,line:int)->BusRoute:
        return self.__bus_route[line]
        
    def display_c(self):
        for bus in self.__bus_route:
            self.__bus_route[bus].display_r()

    #adds object from type busroute (class) to bus_route dict:
    def add_route(self, line_num, origin, destination, list_stops) -> bool:
        if line_num in self.__bus_route:
            return False
        b = BusRoute(line_num, origin, destination, list_stops)
        self.__bus_route[line_num] = b
        return True















