#!/usr/bin/env python


def longest_recursive(string1:str,strings_list:list)->str: 
    if(len(string1) == 0):
        return ''
        
    longest = ''
    print('string1: ',string1,' len: ',len(string1),strings_list)
    for i in range(1,len(string1)+1):
        currentstr = string1[0:i]
        # print('i= ',i,'currentstr: ',currentstr )
        for s in range(len(strings_list)):
            if strings_list[s].find(currentstr) == -1:
                longnext = longest_recursive(string1[1:len(string1)],strings_list)
                return longnext if(len(longnext) > len(longest)) else longest
        longest = currentstr 
    longnext = longest_recursive(string1[1:len(string1)],strings_list)
    return longnext if(len(longnext) > len(longest)) else longest

    
strings = ['rabcde','dabcdegr','rrrabcdeftr']
st = strings[0]

print(st,strings[1:len(strings)])
abc = longest_recursive(st,strings[1:len(strings)])
print('abc=',abc)

 