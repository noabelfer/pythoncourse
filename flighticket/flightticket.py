flightclass = {
    'Busness': {
      "seats": {('A','D'):55,('B','C'):0},
       "meal": {'Luxury':55,'Business':0,'Economy':0},
       "legroom": {():0},
       "lines": {(5,7): 3000,(8,10): 2300},
       "luggage":{'limit':50,'price':10}
    },
    'Economy': {
        "seats": {('A','D'):10,('B','C'):0},
        "meal": {'Luxury':42,'Business':22,'Economy':7},
        "lines": {(11,20): 1700,(21,40): 1500,(41,60): 1300},
        "legroom":{(12,22,42):15},
        "luggage":{'limit':20,'price':10}          
    }
}


def line_get(cls:str,line:int)->tuple:
    linestuples = flightclass.get(cls).get('lines').keys();
    for item in linestuples:
        if(line >= item[0] and line <= item[1]):
            return (line,flightclass.get(cls).get('lines').get(item))
    return ()

def line_options_get(cls:str)->str:
    linestuples = flightclass.get(cls).get('lines').keys();
    st =""
    for item in linestuples:
        price = flightclass.get(cls).get('lines').get(item)
        st += ('For lines {it} price is: {pr}\n'.format(it=item,pr=price))
    return st



def seat_get(cls:str,chair:str)->tuple:
    seatslist = flightclass.get(cls).get('seats').keys();
    print(seatslist)
    for item in seatslist:
        print('itemmm ',item)
        if(chair in item):
           return (chair,flightclass.get(cls).get('seats').get(item))
    return ()

def seat_options_get(cls:str)->str:
    seat = flightclass.get(cls).get('seats')
    st = "For "+cls+" the price for seat "+str(seat)
    return st

   
def meal_get(cls:str,meal:str)->tuple:
    price = flightclass.get(cls).get('meal').get(meal)
    return (meal,price)

    
def meal_options_get(cls:str)->str:
    meals_key = list(flightclass.get(cls).get('meal').keys())
    meals_options = flightclass.get(cls).get('meal')
    for i in range(1,len(meals_key)+1):
        meal_name = meals_key[i-1]
        meal_price = meals_options.get(meal_name)
        print(f" {i}  {meal_name} price {meal_price}")
##    st = "For "+cls+" the price is "+str(price)
    return "  "
    
def luggage_get(cls:str,kilo:int)->tuple:
    limit = flightclass.get(cls).get('luggage').get('limit')
    price = flightclass.get(cls).get('luggage').get('price')
    if(kilo > limit):
        return (kilo,(kilo-limit) * price)
    return ()

def luggage_options_get(cls:str)->str:
    limit = flightclass.get(cls).get('luggage').get('limit')
    price = flightclass.get(cls).get('luggage').get('price')
    st = 'For {cl} the price extra on exceeding {lim}Kg is {pri}$ per Kg'.format(cl=cls,lim=limit,pri=price)
    return st
    
def legroom_get(cls:str,line:int)->tuple:
    legstuples = flightclass.get(cls).get('legroom').keys()
    for leg in legstuples:
        return (line,flightclass.get(cls).get('legroom').get(leg))
    return ()

    
def legroom_options_get(cls:str)->str:
    legstuples = flightclass.get(cls).get('legroom').keys()
    for leg in legstuples:
        price = flightclass.get(cls).get('legroom').get(leg)
        st = 'For lines: {t} price is: {p}'.format(t=leg,p=price)
        return st  
    return "No roomlegs available"

meal_options_get('Economy')