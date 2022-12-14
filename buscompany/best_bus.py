from typing import Type
from busroute import BusRoute
from select import print_dict
from select import dict_2_str

class BestBusCompany:

    def __init__(self):
        self.__bus_route: {BusRoute} = {}
        
    def __str__(self):
        st =  'Bus company details:\n'
        st += '--------------------\n'
        return st+dict_2_str(self.get_as_dict(True),0)
        
    def display_no_driver_name(self):
        print('Bus company details:')
        print('--------------------')
        print_dict(self.get_as_dict(False),0)
        
    def line_used(self,line:int)->bool:
        return line in self.__bus_route
    
    def BusRoute(self,line:int)->BusRoute:
        return self.__bus_route[line]
          
    def get_as_dict(self,with_driver_name:bool):
        mydict = {}
        for item in self.__bus_route:
            mydict['line '+str(item)] = self.__bus_route[item].get_as_dict(with_driver_name)
        return mydict
        
    #adds object from type busroute (class) to bus_route dict:
    def add_route(self, line_num, origin, destination, list_stops) -> bool:
        if line_num in self.__bus_route:
            return False
        b = BusRoute(origin, destination, list_stops)
        self.__bus_route[line_num] = b
        return True
        
    def del_route(self, line_num:int) -> bool:
        if not line_num in self.__bus_route:
            return False
        b = self.__bus_route.pop(line_num)
        return True















