various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]

for n in various:
    item = str(type(n)).replace("<class '","").replace("'>","")
    print (f' {n} {item} ')
