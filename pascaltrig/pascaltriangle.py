def factorial(n):
    if(n==0):
        return 1
    return n * factorial(n-1)
  
def nCr(n:int,r:int)->int:
# # nCr = n!/((n-r)!*r!)
    return factorial(n)//(factorial(r)*factorial(n-r)) 

def pascaltrig(n:int):
    for i in range(n):
        for j in range(n-i+1):
     
            # for left spacing
            print(end=" ")
     
        for j in range(i+1):
     
            # nCr = n!/((n-r)!*r!)
#           print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            print(nCr(i,j), end=" ")
        # for new line
        print()

    
def pascaltriglist(n:int):
    out = []
    for i in range(n):
        outi = []     
        for j in range(i+1):  
            # nCr = n!/((n-r)!*r!)
  #          print(f' i = {i} j = {j}')
 #           outi.append(factorial(i)//(factorial(j)*factorial(i-j)))
            outi.append(nCr(i,j))
        out.append(outi)
    return out 

pascaltrig(10)
mylist = pascaltriglist(10)
for pasitem in mylist:
    print(pasitem)