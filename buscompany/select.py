

def select(msg:str,n_options:int)->int:
    print(msg)
    while(True):
        ch = input('Select 1 to: '+str(n_options)+'> ')
        if not ch.isnumeric():
            print('Error input format ')
            continue
        chint = int(ch)
        if chint >=1 and chint <= n_options:
            return chint
        print("Selection not in range!")
        continue
        
def print_dict(mydic:dict,offset:int):
    for key,values in mydic.items():
        for i in range(offset):
            print(' ', end='')
        print(key,' : ', end='')
        if isinstance(values,dict):
            print()
            print_dict(values,offset+8)
        else:
            print(values)