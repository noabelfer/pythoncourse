#!/usr/bin/env python



def longest_str(string1:str,strings_list:list)->str:   
    longest = ''
    for i in range(len(string1)+1):

        currentstr = string1[0:i]
        for s in range(len(strings_list)):
            if strings_list[s].find(currentstr) == -1:
                return longest
        longest = currentstr 
    return longest

def longest_all(string1:str,strings_list:list)->str:
    longlong = ''
    st = string1
    while(len(st) > 0):
        sss = longest_str(st,strings_list)
        if(len(sss) > len(longlong)):
            longlong = sss
        st = st[1:len(st)]
    return longlong
    
strings = ['rabcde','dabcdegr','rrrabcdeftr']
st = strings[0]
print(st,strings[1:len(strings)])

long_long = longest_all(st,strings[1:len(strings)])
print('the longets',long_long)

 