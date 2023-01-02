class grid:
    DIMS:int
    CELL_WIDTH:int = 10
    arr = []
    marker = {0: ' ',1: 'X', 2:'O'}
    
    def __init__(self,dimensions):
        self.DIMS = dimensions   
        self.arr = [[0 for i in range(self.DIMS)] for j in range(self.DIMS)]
        self.fill()
    
    def __str__(self):
        return str(self.arr) 

    
    def fill(self):
        for i in range(0,self.DIMS):
            for j in range(0,self.DIMS):
                self.arr[i][j] = 0
    ################# access methods ###########
    def put(self,ro,co,user):
        self.arr[ro-1][co-1] = user
        
    def get(self,ro,co)->int:
        return self.arr[ro-1][co-1]
    ######################  display methods ###########
    def print_hor(self):
        print('|_________'*self.DIMS,end='')
        print('|')
        
    def print_top(self):
        print(' ', end='')
        print('__________'*self.DIMS)
        
    def print_blank(self):
        print('|         '*self.DIMS,end='')
        print('|')
        
    def print_row(self,row):
        for col in range(0,self.DIMS):
            print('|   ',self.marker[int(self.arr[row][col])],'   ', end='')
        print('|')
  
        
#         print_top(self)
# ______________________________   
# |         |         |         | print_blank()
# |   1     |   2     |   3     | display()
# |_________|_________|_________| print_blank()
# |         |         |         |
# |   2     |   4     |   6     | 
# |_________|_________|_________| print_hor()
# |         |         |         | print_blank()
# |   3     |   6     |   9     |
# |_________|_________|_________| print_hor()       
    
    def display(self):
        self.print_top()
        for i in range(0,self.DIMS):
            self.print_blank()
            self.print_row(i)
            self.print_hor()
   
    def display2(self):
        for i in range(0,self.DIMS): 
            print(str(self.arr[i]))
            
my_grid = grid(5)
my_grid.put(1,5,1)
my_grid.put(3,3,1)
my_grid.put(5,1,2)
print(my_grid)
print()
my_grid.display2()
print()
my_grid.display()
print()            
