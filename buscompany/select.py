

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