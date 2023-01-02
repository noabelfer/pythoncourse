SCHEMA1 = "ABC DEFGH IJK"
##########################
SEAT1 = "34J"
CHAIR = SEAT1[-1]
RAW = SEAT1[0:-1]
print(f'raw {RAW} CHAIR {CHAIR}')
index = SCHEMA1.rfind(CHAIR)
FIRST = SCHEMA1[0]
LAST = SCHEMA1[-1]
position = ""
if (CHAIR == FIRST or CHAIR == LAST ):
    position = "window"
elif (SCHEMA1[index-1]==' ') or (SCHEMA1[index+1]==' '):
    position = "aisle"
else:
    position = "middle"

print(f'SCHEMA <{SCHEMA1}> ticket chair <{SEAT1}>  raw {RAW} chair {CHAIR} position {position}')
