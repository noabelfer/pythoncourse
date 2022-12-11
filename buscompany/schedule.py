from datetime import datetime


class ScheduledRides:
    def __init__(self, origin_time:int, destination_time:int, driver_name:str):
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays:list = [int]

    def __str__(self):
        st = "origin: "+str(self.origin_time) + " destination: " + str(self.destination_time) + " driver: " + self.driver_name
        return st

