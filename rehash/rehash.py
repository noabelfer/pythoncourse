


def rehash(inp:list,rows:int,cols:int)->list:
    rlen = len(inp)
    clen = len(inp[0])
    if(rlen * clen != rows * cols):
        return inp 
    flat = []
    for i in range(rlen):
        for j in range(clen):
            flat.append(inp[i][j])
            
    out = []
    c = 0
    for i in range(rows):
        outline = []
        for co in range(cols):
            outline.append(flat[c])
            c += 1
        out.append(outline)
    return out
        
    
print("1,4")
a = rehash([[1,2],[3,4]],1,4)
print(a)
print("4,1")
a = rehash([[1,2],[3,4]],4,1)
print(a)
print("5,4")
a = rehash([[1,2,3,4,5],[6,7,8,9,10],[100,200,300,400,500],[1000,200,3000,4000,5000]],5,4)
print(a)
print("2,10")
a = rehash([[1,2,3,4,5],[6,7,8,9,10],[100,200,300,400,500],[1000,200,3000,4000,5000]],2,10)
print(a)
print("10,2")
a = rehash([[1,2,3,4,5],[6,7,8,9,10],[100,200,300,400,500],[1000,200,3000,4000,5000]],10,2)
print(a)