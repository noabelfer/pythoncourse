import turtle

mycolor:bool = False  
DIMS =5
LENGTH = 100 
start_raw:int 
arr = [[0 for i in range(DIMS)] for j in range(DIMS)]
game_over:bool = False

def screen_2_x(x:int)->int: return int((x-start_raw)//LENGTH +1)
def x_2_screen(x:int)->int: return int(start_raw + x * LENGTH - LENGTH/2)
def screen_2_y(y:int)->int: return int(DIMS-((y-start_raw)//LENGTH))
def y_2_screen(y:int)->int: return int((start_raw + (LENGTH//2) + (DIMS*LENGTH)) - (y*LENGTH))

def print_arr():
    global arr
    for row in arr:
        print(row)
        
def fxn(x, y):
    global mycolor
    global game_over
    print(x,y)
    colordot = ('blue','red')
    turtle.penup()
    xx:int = screen_2_x(x)
    yy:int = screen_2_y(y)
    print('x=',xx,'y=',yy)
    xxx = x_2_screen(xx)
    yyy = y_2_screen(yy)
    print('xxx=',xxx,'yyyy=',yyy)
    turtle.goto(xxx,yyy)

    if game_over:
        print("Game is over");
        return        
    if(xx < 1) or (xx > DIMS) or (yy < 1) or (yy > DIMS):
        print("out of range");
        return 
    if(arr[yy-1][xx-1] != 0):
        print("Already occupy")
        return

    arr[yy-1][xx-1] = 1 + int(mycolor)
    print_arr()
    turtle.pendown()
    turtle.dot(20,colordot[int(mycolor)])
    turtle.penup()
    mycolor = not mycolor 
    chk = check_arr()
    print('check_arr ',chk)
    draw_winning_line(turtle,chk)

    
def draw_winning_line(t:turtle,result:tuple):
    global game_over
    print('result ',result)
    src:tuple
    dst:tuple
    match result[0]:
        case 'raw':
            src = (x_2_screen(1),y_2_screen(result[1]))
            dst = (x_2_screen(DIMS),y_2_screen(result[1]))
        case 'col':
            src = (x_2_screen(result[1]),y_2_screen(1))
            dst = (x_2_screen(result[1]),y_2_screen(DIMS))
        case 'left':
            src = (x_2_screen(1),y_2_screen(1))
            dst = (x_2_screen(DIMS),y_2_screen(DIMS))
        case 'right':
            src = (x_2_screen(DIMS),y_2_screen(1))
            dst = (x_2_screen(1),y_2_screen(DIMS))
        case 'teko':
            t.penup()
            t.goto((-LENGTH,-LENGTH))
            turtle.write('Teko', font=("Verdana",30, "normal"))
            game_over = True
            return
        case _:
            return
    t.goto(src)
    t.pendown()
    t.goto(dst)
    t.penup()
    t.goto((-LENGTH,-LENGTH))
    st = "User "
    st += str(result[2])
    st += " wins!!"
    turtle.write(st, font=("Verdana",30, "normal"))
    t.hideturtle()
    t.ht()
    game_over = True
    
def grid(t:turtle,length:int,dim:int):
    global start_raw
    print("start")
    start_raw = -dim//2 *length
    start_col = -dim//2 *length
  
    print("start loop")
    for i in range(0,dim+1):
        print("i",i)
        t.penup()
        t.goto(start_col,i * length+start_raw)
        t.pendown()
        t.goto(start_col+(length*dim),i * length+start_raw)
    for i in range(0,dim+1):
        print("i",i)
        t.penup()
        t.goto(length*i+start_col,start_raw)
        t.pendown()
        t.goto(length*i+start_col,length*dim+start_raw)
    t.penup()
    
def check_raw(c:int)->int:
    first = arr[c][0]
    if(first == 0):
        return 0
    for ch in arr[c]:
        if(ch != first):
            return 0
    return first 

def check_col(c:int)->int:
    first = arr[0][c]
    if(first == 0):
        return 0
    for craw in range(DIMS):
        if(first != arr[craw][c]):
            return 0
    return first 

def check_left()->int:
    first = arr[0][0]
    if(first == 0):
        return 0
    for i in range(DIMS):
        if(first != arr[i][i]):
            return 0
    return first 
    
def check_right()->int:
    first = arr[DIMS-1][0]
    print('first ',first)
    if(first == 0):
        return 0
    for i in range(DIMS):
        print('DIMS-i',DIMS-i-1,' i ',i)
        if(first != arr[DIMS-i-1][i]):
            return 0
    return first 

def check_teko()->bool:
    for row in range(DIMS):
        for col in range(DIMS):
            if arr[row][col] == 0:
                return False
    return True 
    
def check_arr()->int:
    for raw in range(DIMS):
        c = check_raw(raw)
        if (c > 0):
            print('raw ',raw+1)
            return ('raw',raw+1,c)
    for col in range(DIMS):
        c = check_col(col)
        if (c > 0):
            print('col ',col+1)
            return ('col',col+1,c)
    c = check_left()
    if c > 0:
        return ('left',0,c)
    c = check_right()
    if c > 0:
        return ('right',0,c)
    if(check_teko()):
        return ('teko',0,0)
    return ('none',0,0)
tina = turtle.Turtle()
turtle.title("Targil x mix drix by Noa Madar")
tina.speed(10)
##tina.shape("turtle")
tina.hideturtle()
tina.ht()
wn = turtle.Screen()
grid(tina,LENGTH,DIMS)

wn.onclick(fxn)
wn.mainloop()
