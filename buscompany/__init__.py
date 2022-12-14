from best_bus import BestBusCompany
from menusystem import CompanyServices
from  select import dict_2_str
from  select import print_dict


if __name__ == '__main__':
    company = BestBusCompany()
#    service = CompanyServices(company)
#    service.menu_engine()
    company.add_route(4,'telaviv','raanana',['petach tikva','morasha','kfar saba'])
    print(company)

    company.get_busriute(4).add_schedule(9,10,'moshe')
    company.get_busriute(4).add_schedule(11,12,'dan')
    company.get_busriute(4).add_schedule(15,16,'jon')
#    print(company.get_busriute(4))
    company.add_route(5,'haifa','jerusalem',['hedera','rannana'])
    company.get_busriute(5).add_schedule(9,10,'josh')
    company.get_busriute(5).add_schedule(11,12,'dan')
    company.get_busriute(5).add_schedule(15,16,'shos')
    print(company)
#    company.display_c()
#    line5dict = company.get_busriute(5).get_as_dict(True)
 #   print('--------------------dic-----------')
 #   print(line5dict)
