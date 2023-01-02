class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                 int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#                 print(f'{s[i]} rom_val[s[{i}]] {rom_val[s[i]]} rom_val[s[{i - 1}] {rom_val[s[i - 1]]} int_val {int_val}')
            else:
                int_val += rom_val[s[i]]
#                print(f'{s[i]} rom_val[s[{i}]] {rom_val[s[i]]} int_val {int_val}' )
                
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMCMLXXXIV'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))
