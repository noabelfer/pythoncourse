


def addmatch(inp:list,n:int)->list:
    org = inp
 #   print(f'org({n}): {org} ')
    candidates = []
    if(n == 0):
        return org
    for i,v in enumerate(inp):
        if(v == 1):
            continue
        if(i==0) and (inp[1] == 0):
            candidates.append(i)
            continue
        if(i==(len(inp)-1) and inp[i-1] == 0):
            candidates.append(i)
            continue
        if(inp[i-1] == 0) and (inp[i+1] == 0):
            candidates.append(i)
 #   print('candidates ',candidates)
    if (len(candidates) < n):
        return []
    org[candidates[0]] = 1
    return addmatch(org,n-1)
  
        

print("[0, 1, 1, 0, 0, 0 ,0 ,0, 1, 0, 0, 0, 0],3")      
a = addmatch([0,1,1,0,0,0,0,0,1,0,0,0,0],3)
print(a)

print("[0, 1, 1, 0, 0, 0 ,0 ,0, 1, 0, 0, 0, 0],4")      
a = addmatch([0,1,1,0,0,0,0,0,1,0,0,0,0],4)
print(a)

print("[0, 1, 1, 0, 0, 0 ,0 ,0, 1, 0, 0, 0, 0],5")      
a = addmatch([0,1,1,0,0,0,0,0,1,0,0,0,0],5)
print(a)
print("[0, 1, 1, 0, 0, 0 ,0 ,0, 1, 0, 0, 0, 0],6")      
a = addmatch([0,1,1,0,0,0,0,0,1,0,0,0,0],6)
print(a)