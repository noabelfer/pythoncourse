

def binsearch(binstring:str)->int:
    search = '01'
    count  = 0
    while len(search) <= len(binstring):
        n1 = binstring.count(search)
        n2 = binstring.count(search[::-1])
        if((n1+n2) == 0):
            break 
        count += (n1+n2)
        search = '0'+search+'1'
    return count
        
print('10101111000: '+str(binsearch('10101111000')))

print('00110011: '+str(binsearch('00110011')))    

print('10101: '+str(binsearch('10101')))    
