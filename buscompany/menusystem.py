from best_bus import BestBusCompany
from select import select

class CompanyServices:
    msgs_dic ={
        'msgtop': 'Welcome please select \n1. for manager \n2. for customer',
        'msgmng':  'Please select one of the following manager options: \n1. Add route  \n2. Delete row \n3. Update row \n4. Add schedule ride',
        'msg_stop_or_cont': 'Please select 1 to continue 2 to quit',
        'msgpsng': 'Please select one of the following passenger options: \n1. Search by line  \n2. Search by origin \n3. Search by destination \n4. Search by bus stop \n5. Report delays'
        }
    def __init__(self,company:BestBusCompany):
        self.__company:BestBusCompany = company
        
    def none_f(self):
        print("none_f")

    def chk_pswd_f(self):
        print("chk_pswd_f")

    def add_route_f(self):
        print("add_route_f")
        
    def del_route_f(self):
        print("del_route_f")

    def upd_route_f(self):
        print("upd_route_f")

    def add_sched_f(self):
        print("add_sched_f")

    def quit_f(self):
        print("quit_f")
        exit()
        
    def srch_line_f(self):
        print("srch_line_f")
        
    def srch_orig_f(self):
        print("srch_orig_f")
        
    def srch_dest_f(self):
        print("srch_dest_f")
        
    def srch_stop_f(self):
        print("srch_stop_f")
        
    def rprt_delays_f(self):
        print("rprt_delays_f")
       
    func_dict = {
        'none_f': none_f,
        'chk_pswd_f' : chk_pswd_f,
        'add_route_f' : add_route_f,
        'del_route_f': del_route_f,
        'upd_route_f': upd_route_f,
        'add_sched_f': add_sched_f,
        'quit_f': quit_f ,
        'srch_line_f': srch_line_f,
        'srch_orig_f': srch_orig_f,
        'srch_dest_f': srch_dest_f,
        'srch_stop_f': srch_stop_f,
        'rprt_delays_f': rprt_delays_f
        }

    nav = {
            'top': {'msg': 'msgtop','opts': 2,'act': 'none_f'   ,'next': {1: 'mng',2: 'psngr'}},
            'mng': {'msg': 'msgmng','opts': 4,'act': 'chk_pswd_f','next': {1: 'add_route',2: 'del_route',3: 'upd_route',4: 'add_sched'}},
            'mng2':{'msg': 'msgmng','opts': 4,'act': 'none_f','next': {1: 'add_route',2: 'del_route',3: 'upd_route',4: 'add_route'}},
            'add_route': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'add_route_f','next': {1:'mng2',2: 'quit'}},
            'del_route': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'del_route_f','next': {1:'mng2',2: 'quit'}},
            'upd_route': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'upd_route_f','next': {1:'mng2',2: 'quit'}},
            'add_sched': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'add_sched_f','next': {1:'mng2',2: 'quit'}},
            'quit': {'msg': 'msg_stop_or_cont','opts': 0,'act': 'quit_f','next': {}},
            'psngr': {'msg': 'msgpsng','opts': 5,'act': 'none_f','next': {1: 'srch_line',2: 'srch_orig',3: 'srch_dest',4: 'srch_stop',5: 'rprt_delays'}},
            'srch_line': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'srch_line_f','next': {1:'psngr',2: 'quit'}},
            'srch_orig': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'srch_orig_f','next': {1:'psngr',2: 'quit'}},
            'srch_dest': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'srch_dest_f','next': {1:'psngr',2: 'quit'}},
            'srch_stop': {'msg': 'msg_stop_or_cont','opts': 2,'act': 'srch_stop_f','next': {1:'psngr',2: 'quit'}},
            'rprt_delays':{'msg': 'msg_stop_or_cont','opts': 2,'act': 'rprt_delays_f','next': {1:'psngr',2: 'quit'}}
          }

    def menu_engine(self):
        state = 'top'       
        while(True):
            print('State : ',state)
            CompanyServices.func_dict[CompanyServices.nav[state]['act']](self)
            s = CompanyServices.nav[state]['msg']
            sel = select(CompanyServices.msgs_dic[s],CompanyServices.nav[state]['opts'])
            state = CompanyServices.nav[state]['next'][sel]
    
  