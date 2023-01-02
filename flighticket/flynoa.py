from inspect import getframeinfo, stack

def debuginfo(message):
    caller = getframeinfo(stack()[1][0])
    print("%s:%d - %s" % (caller.filename, caller.lineno, message)) # python3 syntax print

flyingclass = {
'first_class': {
    "seats": {('A', 'D'): 0, ('B', 'C'): 0},
    "meal": {'luxury_menu1': 0, 'luxury_menu2': 0, 'luxury_menu3': 0 },
    "legroom": {(): 0},
    "lines": {(1, 4): 4000},
    "luggage": {'limit': None , 'price': 0}
    },

'business': {
    "seats": {('A', 'D'): 55, ('B', 'C'): 0},
    "meal": {'luxury_menu1': 42, 'luxury_menu2': 42, 'luxury_menu3': 42, 'business': 0},
    "legroom": {(): 0},
    "lines": {(5, 7): 3000, (8, 10): 2300},
    "luggage": {'limit': 50,  'price': 10}
    },

'economy': {
    "seats": {('A', 'F'): 10, ('B', 'C', 'D', 'E'): 0},
    "meal": {'luxury_menu1': 42, 'luxury_menu2': 42, 'luxury_menu3': 42, 'business_menu': 22, 'economy_menu': 7},
    "lines": {(11, 20): 1700,
              (21, 40): 1500,
              (41,60): 1200},
    "legroom": {(12, 22, 42): 15 },
    "luggage": {'limit': 20,  'price': 10},
    "luxury": {'luxury_menu1' : 'STARTER - Roast veal sweetbread, MAIN    - Cornish turbot,  DESERT  - Hazelnut souffle '  ,
               'luxury_menu2' : 'STARTER - Ravioli lobster , MAIN    - 100-Day aged Cumbrian Blue Grey,  DESERT  - Pecan praline ' ,
               'luxury_menu3' : 'STARTER - Scallops from the Isle of Skye , MAIN    - Aynhoe Park fallow deer,  DESERT  - Caramelised apple Tarte Tatin '}}}




luxury_menu1_exp = 'STARTER - Roast veal sweetbread , MAIN    - Cornish turbot,  DESERT  - Hazelnut souffle '
luxury_menu2_exp = 'STARTER - Ravioli lobster , MAIN    - 100-Day aged Cumbrian Blue Grey,  DESERT  - Pecan praline'
luxury_menu3_exp = 'STARTER - Scallops from the Isle of Skye , MAIN    - Aynhoe Park fallow deer,  DESERT  - Caramelised apple Tarte Tatin '

def get_class_name() -> str:
    classtopick = list(flyingclass.keys())
    while True:
        print(f" we have these classes you can pick from:{classtopick}")
        class_chosen = input('please select a class: ')
        if class_chosen in classtopick:
            print (f" great {name}, you chose: {class_chosen} class")
            return class_chosen
        else:
            print('error, choose again')



def meal(my_chosen_class:str) -> tuple:

#add lux explenations to menu
    lux_keys = list(flyingclass.get(my_chosen_class).get('luxury').keys())
    lux_ops = flyingclass.get(my_chosen_class).get('luxury')
#the names of the list of all meals: meals_key (menuluxury1,2 etc.)
    meals_key = list(flyingclass.get(my_chosen_class).get('meal').keys())
    #meals_options = the tuple of the meal name and price
    meals_options = flyingclass.get(my_chosen_class).get('meal')
    print(f'in {my_chosen_class} class you can choose from these menues, if you wish to have a luxury menu by chef Gordon Ramzi, \n '
          f'please see the luxury menues bellow: ')
    print(lux_ops)
    for i in range(1,len(meals_key)+1):
        meal_name = meals_key[i-1]
        meal_price = meals_options.get(meal_name)

        print(f" {i}  {meal_name} price {meal_price}$")
        # if meal_name in lux_keys:
        #     print(flyingclass.get(my_chosen_class).get('luxury').values())
    while True:
        meal_chosen = int(input('please pick a meal number from the list above: '))
        if meal_chosen > 0 and meal_chosen <= len(meals_key):
            meal_user_chose = meals_key[meal_chosen-1]
            meal_user_price =  meals_options.get(meal_user_chose)
            print(f'great choice, {name}, you chose {meal_user_chose} and the price for it is: {meal_user_price}$')
            return (meal_user_chose, meal_user_price)
        print ('error, please type again the number of menu: ')


def lines(my_chosen_class:str) -> tuple:
    legroom_ops = flyingclass.get(my_chosen_class).get('legroom')
    legroom_list = list(legroom_ops.keys())
    lines_opt = flyingclass.get(my_chosen_class).get('lines')
    lines_list = list(lines_opt)
    while True:
        print(f" these are the lines you can choose from in {my_chosen_class}, {lines_opt}:")
        print("lenlust ",legroom_list)
        if(legroom_list != [()]):
            print(f" these are the legroom lines {legroom_ops}:")
        line_chosen = int(input('please choose a line: '))
        found = False
        for key in lines_list:
            if(line_chosen >= key[0] and line_chosen <= key[1]):
                line_price = lines_opt.get(key)
                found = True
                print('key ',key,'val ',line_price)

                print(f" you chose line number:{line_chosen}  ")
                for item in legroom_list:
                    if line_chosen in item:
                        line_price += legroom_ops.get(item)
                        print(f"this line costs 15$ more,  line:{line_chosen} price:{line_price}")
                        break
                break
        if(not found):
            print("Wrong selection")
            continue
        
        print(line_price)
        return (line_chosen,line_price)


##extra leg room in economy class





def seats (my_chosen_class:str) -> tuple:
    while True:
        seats_op = flyingclass.get(my_chosen_class).get('seats')
        print(seats_op)
        seat_chosen = input('please choose a seat: ')
        for key, v2 in seats_op.items():
            seat_cost = v2
            print(f" the fee for this seat is:{seat_cost}$")
            return (seat_chosen, seat_cost)



def luggage(my_class):
    while True:
        lug_extra = 0
        isluggage = input('would you like to add any luggage? type y/n: ')
        if isluggage == 'n':
            return lug_extra
        if isluggage == 'y':
            while True:
                lug_lim = flyingclass[my_class]['luggage']['limit']
                lug_ex_price = flyingclass[my_class]['luggage']['price']
                print(f'your limit is {lug_lim} and the cost for every extra kg is {lug_ex_price}')

                if my_class != 'first_class':
                    luggage_w = int(input('what is the weight of you luggage? '))
                    if luggage_w > lug_lim:
                        lug_extra += (luggage_w - lug_lim) * (lug_ex_price)
                print(f"the total fee for your luggage is:{lug_extra}")
                return lug_extra


def prRed(skk): print("\033[91m {}\033[00m".format(skk))

def prGreen(skk): print("\033[92m {}\033[00m".format(skk))

def prYellow(skk): print("\033[93m {}\033[00m".format(skk))

def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))

def prPurple(skk): print("\033[95m {}\033[00m".format(skk))

def prCyan(skk): print("\033[96m {}\033[00m".format(skk))



if __name__ == "__main__":

    print('economy',lines('economy'))
    print('business',lines('business'))
    exit()

    prPurple("------WELCOME TO NOA'S AIRLINES------")
    name:str = input('please enter your name')
    destination = input('where are we flying to?')
    my_class = get_class_name()
    meal_user_price_and_name = meal(my_class)
    line_price = lines(my_class)
    seat_cost = seats(my_class)
    lug_extra = luggage(my_class)

    print(f" meal = {meal_user_price_and_name[0]} price = {meal_user_price_and_name[1]}")


