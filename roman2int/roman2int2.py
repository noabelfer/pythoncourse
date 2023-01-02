class py_solution:
    def roman_to_int(self, s:str)->int:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sign_mul = []
        
        for i in range(len(s)-1):
            if(rom_val[s[i]] < rom_val[s[i+1]]):
                sign_mul.append(-1)
            else:
                sign_mul.append(1)
        sign_mul.append(1)
        
        

        int_val = 0
        for i in range(len(s)):
            int_val += sign_mul[i] * rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMCMLXXXIV'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))
