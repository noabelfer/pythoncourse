
def sortstrings(inp):
    in1:list = inp.split('-')
    in1.sort()
    out:string = ""
    if(len(in1) > 1):
        out = (in1[0])
    else:
        return "noinput"
    for item in range(1,len(in1)):
        out += ("-")
        out += (in1[item])
    return out 
    
    
str2 = sortstrings("green-black-red-white-yellow")
print(str2)
str2 = sortstrings("")
print(str2)


