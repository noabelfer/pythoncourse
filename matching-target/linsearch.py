list_nums:list = []
for i in range(1,101):
    list_nums.append(i)
targetnum:int = 199

list_ind = []
count = 0
for i in range(0,len(list_nums)-1):
    for j in range(i+1, len(list_nums)):
        count += 1
        if targetnum == (list_nums[i] + list_nums[j]):
            list_ind.append(i)
            list_ind.append(j)
            break
print(list_ind)
print('Count: ',count)