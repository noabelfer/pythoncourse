from best_bus import BestBusCompany
from menusystem import CompanyServices
from  select import dict_2_str
from  select import print_dict



if __name__ == '__main__':
    company = BestBusCompany()

    company.add_route(4,'telaviv','raanana',['petach tikva','morasha','kfar saba'])
    print(company)
    company.BusRoute(4).add_schedule(9,10,'moshe')
    company.BusRoute(4).add_schedule(11,12,'dan')
    company.BusRoute(4).add_schedule(15,16,'jon')
    print(company.BusRoute(4))
    company.add_route(5,'haifa','jerusalem',['hedera','rannana'])
    company.BusRoute(5).add_schedule(9,10,'josh')
    company.BusRoute(5).add_schedule(11,12,'dan')
    company.BusRoute(5).add_schedule(15,16,'shos')
    print(company)
    service = CompanyServices(company)
    service.menu_engine()
