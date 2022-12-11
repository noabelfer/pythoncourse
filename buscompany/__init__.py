import best_bus

if __name__ == '__main__':
    company = best_bus.BestBusCompany()
    company.add_route(4,'telaviv','raanana',['petach tikva','morasha','kfar saba'])
    company.add_schedule(4,9,10,'moshe')
    company.add_schedule(4,11,12,'dan')
    company.add_schedule(4,15,16,'jon')
    company.add_route(5,'haifa','jerusalem',['hedera','rannana'])
    company.add_schedule(5,9,10,'josh')
    company.add_schedule(5,11,12,'dan')
    company.add_schedule(5,15,16,'shos')
    company.display_c()

