


coffee_list = ['espresso', 'doppio', 'lungo', 'ristretto', 'macchiato',
               'corretto', 'con panna', 'romano', 'cappuccino', 'americano',
               'cafelatte','flat white', 'marocchino', 'mocha', 'bicerin', 'breve',
               'raf coffee', 'mead raf', 'vienna coffee', 'chocolate milk', 'latte macchiato',
               'glace', 'freddo', 'irish coffee','frappe', 'cappuccino fredo', 'caramel frape',
               'espresso lacino']
#
# This function returns list of [hours,minutes]
#
def  gethoursminutes()->list:
    newinttime =[]
    while True:
        print("=============HH:YY");
        time = input('insert time: ')
        newtime = time.split(':')
        if(len(newtime) != 2):
            print("Wrong time format")
            continue
        if((not newtime[0].isnumeric()) or (not newtime[0].isnumeric())):
            print("Wrong time format")
            continue
        newinttime.append(int(newtime[0]))
        newinttime.append(int(newtime[1]))
        
        if((newinttime[0] < 0) or (newinttime[0] > 23) or (newinttime[1] < 0) or (newinttime[1] > 59)):
            print("Time input is out of range")
            continue
        return newinttime
#
# Returns int where the returns int value 
#   Params:  
#          int lowlimit - The low limit of the returned value 
#          dtring msg - The message presented to the user
#
def getnumber(lowlimit: int,msg )->int:
    while True:
        str1 = input(msg)
        if (not str1.isnumeric()):
            print('Wrong input number try again')
            continue

        n = int(str1)
        if (n < lowlimit):
            print('Number should be greater than ',lowlimit)
            continue  
        return n
#
#   Return list of int or empty list in case the user type "skip"
#         the returned list sorted in desending order .
#
def getexcludes()->list:
    coffee_int_2 = []
    while True:
        exclude_coffee= input("enter the coffee numbers you would like to exclude seperated by , or skip : ")
        if(exclude_coffee == "skip"):
            return coffee_int_2
        list_coffee_exclude = exclude_coffee.split(',')
        numericok = True
        for intitem in list_coffee_exclude:
            if not intitem.isnumeric():
                print("Wrong input")
                continue
        coffee_int = []
        ##print(list_coffee_exclude)
        for i in range(0,len(list_coffee_exclude,)):
            coffee_int.append(int(list_coffee_exclude[i]))
        ###print(coffee_int)
        coffee_int_2 = coffee_int.copy()
        coffee_int_2.sort(reverse=True)
###        print(coffee_int_2)
        return coffee_int_2
############ global variables ###############################
hours = 0
minutes = 0
n_coffefriends = 0  
########### program start ###################################      
# Step 1 get the time       
readtime = gethoursminutes()
hours = readtime[0]
minutes = readtime[1]
# Step 2 get number of coffe friends
n_coffefriends = getnumber(1,"Please enter number of coff riends: ")
print('n_coffefriends ',n_coffefriends)
#bonus 1
add_number = getnumber(0,"Please enter coff shift: ")

#bonus 2
coffe_exclude_list = getexcludes()
###print(coffe_exclude_list)

if(len(coffe_exclude_list) > 0):
    for i in range(len(coffe_exclude_list)):
        coffee_list.pop(coffe_exclude_list[i])


# step 3 compute coffee for each friend and print
####print(coffee_list)
print('Friend   Coffe')
print('======   ============')
for i in range(n_coffefriends):
    coffe_index = ((hours + add_number) + i * minutes) % len(coffee_list)
    coffee = coffee_list[coffe_index]
    friend_number = str(i)
    friend_number = '{:>6}'.format(friend_number)
    print(f'{friend_number}   ({coffe_index}) {coffee}')


