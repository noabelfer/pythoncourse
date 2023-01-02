# Step 1 get the time
coffee_list = ['espresso', 'doppio', 'lungo', 'ristretto', 'macchiato',
               'corretto', 'con panna', 'romano', 'cappuccino', 'americano',
               'cafelatte','flat white', 'marocchino', 'mocha', 'bicerin', 'breve',
               'raf coffee', 'mead raf', 'vienna coffee', 'chocolate milk', 'latte macchiato',
               'glace', 'freddo', 'irish coffee','frappe', 'cappuccino fredo', 'caramel frape',
               'espresso lacino']
#bonus 2
def getexcludes() -> list:
    coffee_int_2 = []
    while True:
        exclude_coffee = input("enter the coffee numbers you would like to exclude seperated by , or skip : ")
        if (exclude_coffee == "skip"):
            return coffee_int_2
        list_coffee_exclude = exclude_coffee.split(',')
        numericok = True
        for intitem in list_coffee_exclude:
            if not intitem.isnumeric():
                print("Wrong input")
                continue
        coffee_int = []
        ##print(list_coffee_exclude)
        for i in range(0, len(list_coffee_exclude, )):
            coffee_int.append(int(list_coffee_exclude[i]))
        ###print(coffee_int)
        coffee_int_2 = coffee_int.copy()
        coffee_int_2.sort(reverse=True)
        ###        print(coffee_int_2)
        return coffee_int_2
        
hours = 0
minutes = 0
n_coffefriends = 0
while True:

    time = input('insert time in format hh:mm ')
    if not ":" in time:
        continue

    newtime = time.split(':')
    h = newtime[0]
    m = newtime[1]

    if ((len(newtime) != 2) or (not h.isnumeric()) or (not m.isnumeric())):
        print('Wrong input time try again')
        continue
    hours = int(h)
    minutes = int(m)
    if ((hours < 0) or (hours > 23) or (minutes < 0) or (minutes > 59)):
        print('Wrong input! time is out of range, try again')
        continue
    break

    # Step 2 get number of coffee friends
while True:
    str1 = input("Please enter number of coffee friends: ")
    if (not str1.isnumeric()):
        print('Wrong input number try again')
        continue

    n_coffefriends = int(str1)
    if (n_coffefriends < 0):
        print('Number should not be negative, try again')
        continue
    break

#bonus 1
add_number = int(input("enter the starting number of the coffee list: "))




coffee_int_2 = getexcludes()
if coffee_int_2 != []:

    
    ### print(coffee_int_2)
    ###print(coffee_list)
    for i in range(len(coffee_int_2)):
        coffee_list.pop(coffee_int_2[i])


# step 3 compute coffee for each friend and print
####print(coffee_list)
print('Friend   Coffe')

for i in range(n_coffefriends):
    coffee = coffee_list[((hours + add_number) + i * minutes) % len(coffee_list)]
    friend_number = str(i)
    friend_number = '{:>6}'.format(friend_number)
    print(f'{friend_number}   {coffee}')