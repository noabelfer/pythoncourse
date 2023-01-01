#

my_bday_dict:dict = {}
def overname(): 
# Too long sentence its preffered to split to more lines 
#    double = input('name already exists. would you like to overwrite it or add a different name? type overwrite or add_different')
#       it mush be clear what the user should type I needed the source to do that .
    print("Name already exists. would you like to overwrite or add a different name?")
    double = input("Type overwrite or add_different: 
 # match case is preffered 
    if double == 'overwrite':
        double_name = input('insert the name you want to rewrite: ')
        newbday = input('please insert a birthday date')
        my_bday_dict.update({double_name: newbday})
    elif (double == 'add_different'):
        insert()
    else:
        print('wrong input. please type again overwrite or add_different')
        overname ()


#Is this function returns string?  select is not defined in this function
def insert():
    print('insert')
    user_name:str = input('please write the name: ')
    bday:str = input('please insert a birthday date')
    if user_name not in my_bday_dict:
        my_bday_dict.update({user_name:bday})
        return select
#The elif not needed because if previous if is true the function returns. if is preffered 
    elif user_name in my_bday_dict:
        # print('name already exists. would you like to overwrite it or add a different name?')
        overname()

def lookup():
    print('lookup')

    name = input('please insert a name: ').strip()
    if name in my_bday_dict.keys():
        print((my_bday_dict[name]),name)
    else:
        relevant_names = [n for n in my_bday_dict.keys() if name in n]
        print(relevant_names)
# if same is 'y' or 'n' you call lookup() anyhow . You use lookup() recursive why?
        if(len(relevant_names)>0):
            same = input(f" did you mean one of these names? {relevant_names} ? y/n ")
            if same == 'y':
                print("please type again")
                lookup()
            if same == 'n':
                print("no such name, please type again")
                # for i in range(len(relevant_names)):
                #     question = input(relevant_names[i])
                lookup()



            #             print((my_bday_dict[n]))
            # if same == 'n':
            #     print('no such name, please try again')
            #     return lookup()


while True: 
### Blank before the input
    select = input("welcome to the birtday Dictionary. Do you want to insert a new BDay or to lookup one?").lower()
    match select:
        case 'insert':
            insert()
        case 'lookup':
            lookup()
        case 'exit':
            print('bye bye')
            break
        case _:
            print('error, please try again')

#    if select == 'insert':
 #       insert()
#    elif select == 'lookup':
#        lookup()
#    elif select == 'exit':
#        print('bye bye')
#        break
 #   else:
 #        print('error, please try again')






