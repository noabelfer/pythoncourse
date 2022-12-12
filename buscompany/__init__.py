from best_bus import BestBusCompany


if __name__ == '__main__':
    company = BestBusCompany()
    company.add_route(4,'telaviv','raanana',['petach tikva','morasha','kfar saba'])
    company.get_busriute(4).add_schedule(9,10,'moshe')
    company.get_busriute(4).add_schedule(11,12,'dan')
    company.get_busriute(4).add_schedule(15,16,'jon')
    company.add_route(5,'haifa','jerusalem',['hedera','rannana'])
    company.get_busriute(5).add_schedule(9,10,'josh')
    company.get_busriute(5).add_schedule(11,12,'dan')
    company.get_busriute(5).add_schedule(15,16,'shos')
    company.display_c()
    line5dict = company.get_busriute(5).get_data(True)
    print('--------------------dic-----------')
    print(line5dict)
