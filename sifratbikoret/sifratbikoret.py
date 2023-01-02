
def countdigits(number):
    i:int =0
    while number> 0:
        number //= 10
        i+= 1
    return i
    
#####################################################
# Return the sum of all digits of decimal number
#  example: if the number is 123 it returns 1+2+3 = 6
#####################################################
def digitssum(number):
    sum = 0 
    while(number > 0):
        sum += number % 10
        number //= 10
    return sum
#############################################
#  Returns sifrat bikoret of a number
#    Sum fo all digits in id as follows:
#       for each digit
#          multiply the digit by its weight 
#          compute its value by digitssum()
#    After sum is computed do  (10-(sum %10))
#############################################     
def sifratbikoret(id:int):  
    id1:int = id
    sum:int = 0
    weight:list = [2,1]
    for i in range (0,8):
        sum += digitssum((id1 % 10) * weight[i%2]) 
        id1 //= 10
    return (10-(sum %10))
 #############################################   
 


    