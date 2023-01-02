class py_solution:
    def roman_to_int(self, s:str)->int:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        keys = list(rom_val.keys())
        for i in range(len(s)):
            if s[i] not in keys:
                print(f'{s[i]} is not roman digit')
                return -1
            
        int_val = 0
        for i in range(len(s)-1):
            if(rom_val[s[i]] < rom_val[s[i+1]]):
                int_val -= rom_val[s[i]]
            else:
                int_val += rom_val[s[i]]
        int_val += rom_val[s[len(s)-1]]
        
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMCMLXXXIV'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))
print(py_solution().roman_to_int('CZ'))