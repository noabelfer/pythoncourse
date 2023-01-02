
count = 0
def binary_search(sor:list,start:int,end:int,t:int):
    global count 
    count +=1 
    mid = (start+end) //2
#    print(f' target {t} start {start} end {end} mid {mid}')
    if(t == sor[mid]):
        return True
    if(start == mid) :
        return(t == sor[end])
    if(t > sor[mid]):
        if(binary_search(sor,mid+1,end,t)):
            return True
    else:
        if(binary_search(sor,start,mid-1,t)):
            return True
    return False
    
target = 199
numbers:int =[]
for i in range(1,101):  
    numbers.append(i)
    
sorted:int = numbers.copy()
sorted.sort()



output = []
for i in range(0,len(numbers)-1):
    if(binary_search(sorted,0,len(numbers)-1,target-numbers[i])):
        output.append(i)
        output.append(numbers.index(target-numbers[i]))
        break
        
print(output)
print('Count: ',count)