

msgs_dic ={
    'msgtop': 'Welcome please select \n1. for manager \n2. for customer',
    'msgmng':  'Please select one of the following manager options: \n1. Add route  \n2. Delete row \n3. Update row \n4. Add schedule ride',
    'msg_stop_or_cont': 'Please select 1 to continue 2 to quit',
    'msgpsng': 'Please select one of the following passenger options: \n1. Search by line  \n2. Search by origin \n3. Search by destination \n4. Search by bus stop \n5. Report delays',

    }
    
def none_f():
    print("none_f")

def chk_pswd_f():
    print("chk_pswd_f")

def add_route_f():
    print("add_route_f")
    
def del_route_f():
    print("del_route_f")

def upd_route_f():
    print("upd_route_f")

def add_sched_f():
    print("add_sched_f")

def quit_f():
    print("quit_f")
    exit()
    
func_dict = {
    'none_f': none_f,
    'chk_pswd_f' : chk_pswd_f,
    'add_route_f' : add_route_f,
    'del_route_f': del_route_f,
    'upd_route_f': upd_route_f,
    'add_sched_f': add_sched_f,
    'quit_f': quit_f 
    }

nav = {
        'top': {'msg': 'msgtop','opts': 2,'act': 'none_f','next': {1: 'mng',2: 'psngr'}},
        'mng': {'msg': 'msgmng','opts': 4,'act': 'chk_pswd_f','next': {1: 'add_route',2: 'del_route',3: 'upd_route',4: 'add_sched'}},
        'mng2':{'msg': 'msgmng','opts': 4,'act': 'none_f','next': {1: 'add_route',2: 'del_route',3: 'upd_route',4: 'add_route'}},
        'add_route': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'add_route_f','next': {1:'mng2',2: 'quit'}},
        'del_route': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'del_route_f','next': {1:'mng2',2: 'quit'}},
        'upd_route': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'upd_route_f','next': {1:'mng2',2: 'quit'}},
        'add_sched': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'add_sched_f','next': {1:'mng2',2: 'quit'}},
        'quit': {'msg': 'msg_stop_or_cont','opts': 0,'act': 'quit_f','next': {}},
        'psngr': {'msg': 'msgpsng','opts': 4,'act': 'none_f','next': {1: 'add_route',2: 'del_route',3: 'upd_route',4: 'add_sched'}},

      }
 
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

state = 'top'       
while(True):
    print('State : ',state)
    func_dict[nav[state]['act']]()
    s = nav[state]['msg']
    sel = select(msgs_dic[s],nav[state]['opts'])
    state = nav[state]['next'][sel]
    
  