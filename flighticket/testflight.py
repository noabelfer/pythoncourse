import flightticket        

#Construct person_ticket
person_ticket = {}
person_ticket['name'] = 'Mr Smith'
clas = 'Economy'
person_ticket['class'] = clas

print("person_ticket name and class");
print(person_ticket)

print('===== Handle line =======') 
option = flightticket.line_options_get(clas)
print(f'line option for class {clas} is: ')
print('-------------------------')
print(option)
print('-------------------------')
li = flightticket.line_get(clas,12)
print("line_options_get : ",li)
person_ticket['line'] = li
print(person_ticket)

print('===== Handle seat =======') 
option = flightticket.seat_options_get(clas)
print(f'seat option for class {clas} is: ')
print('-------------------------')
print(option)
print('-------------------------')
chair = flightticket.seat_get(clas,'D')
print("flightticket.seat_get() : ",chair)
person_ticket['seat'] = chair
print(person_ticket)

print('===== Handle meal =======') 
option = flightticket.meal_options_get(clas)
print(f'meal option for class {clas} is: ')
print('-------------------------')
print(option)
print('-------------------------')
mymeal = flightticket.meal_get(clas,'Luxury')
print("flightticket.meat_get() : ",mymeal)
person_ticket['meal'] = mymeal
print(person_ticket)

print('===== Handle luggage =======') 
option = flightticket.luggage_options_get(clas)
print(f'luggage option for class {clas} is: ')
print('-------------------------')
print(option)
print('-------------------------')
myluggage = flightticket.luggage_get(clas,23)
print("flightticket.luggage_get() : ",myluggage)
person_ticket['luggage'] = myluggage
print(person_ticket)

print('===== Handle legroom =======') 
option = flightticket.legroom_options_get(clas)
print(f'legroom option for class {clas} is: ')
print('-------------------------')
print(option)
print('-------------------------')
mylegroom = flightticket.legroom_get(clas,22)
print("flightticket.luggage_get() : ",mylegroom)
person_ticket['legroom'] = mylegroom
print(person_ticket)
#{'name': 'Mr Smith', 'class': 'Economy', 'line': (12, 1700), 'seat': ('D', 10), 
#'meal': ('Luxury', 42), 'luggage': (23, 30), 'legroom': (22, 15)}
total = person_ticket.get('line')[1]
print('total ',total)
total +=person_ticket.get('seat')[1]
print('total +seat',total)
total +=person_ticket.get('meal')[1]
print('total +meal',total)
total +=person_ticket.get('luggage')[1]
print('total +luggage',total)
total +=person_ticket.get('legroom')[1]
print('total +legroom',total)
person_ticket['total'] = total
print(person_ticket)
print('===== construction of person_ticket ended =======') 

li = flightticket.line_get(clas,112)
if li == ():
    print(' line is out of range')
