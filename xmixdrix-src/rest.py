from datetime import datetime
import time

class Table:
    table_id:int
    seating_cap:int
    is_availble:bool
    time_reservation:datetime
    occupied_seats:int


    def __init__(self,table_id:int, seating_cap:int, is_availble:bool,
                 availble_seats: int):
        print(table_id, seating_cap, is_availble)
        self.table_id = table_id
        self.seating_cap = seating_cap
        self.is_availble = is_availble
        self.availble_seats = availble_seats
        self.time_reservation = datetime.now()
        

    def __str__(self):
        st = "id = " + str(self.table_id) + "  seating_cap = " + str(self.seating_cap) + "  is_availble = " + str(self.is_availble)\
         + "  availble_seats = " + str(self.availble_seats) + " elapsed: "+ str(datetime.now()-self.time_reservation)
        return st

    def reserve(self, num_ppl) -> tuple:
        if self.seating_cap < num_ppl:
            return (False,self.table_id)
        if not self.is_availble:
            return (False,self.table_id)
        self.is_availble = False
        self.availble_seats = self.seating_cap - num_ppl
        self.time_reservation = datetime.now()
        return (True, self.table_id)


    def release(self):
        pass

    def get_time_left(self):
        pass


        #methods:
        #reserve(num_ppl)
        #release
        #get_time_left ->timedelta

        # start_time = datetime.now()
        # limit = datetime.timedelta(hours = 1, minutes= 30)
        # expected_end_time = start_time + limit
        # time_left = expected_end_time - datetime.now()


class Restaurant:
    table_list = []
    num_of_tables = []
    tttt = {}
    def __init__(self, num_of_tables:list):
        self.num_of_tables:list = num_of_tables
        #establish tables
        for i in range (0,len(num_of_tables)):
            self.table_list.append(Table(i,num_of_tables[i],True,0))
            self.tttt[i+1] = Table(i+1,num_of_tables[i],True,0)
            print(self.tttt[i+1])
    print(tttt)
    def status(self):
        for i in self.table_list:
            print(i)

    def reserve(self, num_ppl:int) -> tuple:
        for table in self.table_list:
            t = table.reserve(num_ppl)
            if t[0] :
                return t


    def tables_lst(self, num_of_tables:list):
        return num_of_tables

    def table_taken(self, table_id, ):
        pass

    def free_tables(self,tables_taken ):
        free_tables = [2,3,4]
        return free_tables()


    def table_taken_endtime(self, table_take,):
        pass

if __name__ == '__main__':
    m = datetime.now()
    time.sleep(1)
    mm = m - datetime.now()
    secs = float(m)
    print("sec ",secs)
    # tables = Restaurant([1,2,3,4])
    # print(tables)
    # table1 = Table
    # r = tables.reserve(3)
    rest = Restaurant([3,4,6])
    rest.status()
    rest.reserve(5)
    time.sleep(5)
    rest.status()











