import sifratbikoret
import random

def constructnumber(n:int):
    constnumber:int = 0
    for i in range(0,n):
        m = random.randint(0,9)
        constnumber = constnumber * 10 + m
    return constnumber 
    
personid = input("please enter your id: ")
if(not personid.isnumeric()):
    printf('error input')
    exit()
    
personidnumber = int(personid)

if(personidnumber == 0):
    number:int = constructnumber(8)
    print(f'Bikoret for {number} is: {sifratbikoret.sifratbikoret(number)}')
    exit()
    
if(len(personid) > 8):
    personid = personid[0:8]
    number:int = int(personid)
    print(f'Bikoret for {number} is: {sifratbikoret.sifratbikoret(number)}')
    exit()
    
if(len(personid) < 8):
    n_missing = 8-len(personid)
    number:int = int(personid)
    number2:int = constructnumber(n_missing)
    number = number * (10**n_missing) + number2
    print(f'Bikoret for {number} is: {sifratbikoret.sifratbikoret(number)}')
    exit()

number:int = int(personid)
print(f'Bikoret for {number} is: {sifratbikoret.sifratbikoret(number)}')