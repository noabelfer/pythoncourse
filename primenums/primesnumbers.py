import math
start = 2
end = 12

def isprimenumber(num):
    
    n = int(math.sqrt(num))+1
    
    for i in range(2,n):
        if((num % i) == 0):
            return False ;
    print(f'entry {num} sqrt {n}')
    return True
    
primenumbers = []

for number in range(start,end+1):
    if(isprimenumber(number)):
        primenumbers.append(number)
 
print(primenumbers)