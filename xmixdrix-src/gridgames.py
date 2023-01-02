size = 5
grid = [[col*size+row  for row in range(size)] for col in range(size)]
print("grid : lists of all rows")
for gr in grid:
    print(set(gr))
#grid2 = [[grid[col][row] for col in range(size)] for row in range(size)]
grid2 = [[grid[row][col] for row in range(size)] for col in range(size)]
print("grid2 lists of all columns")       
for gr in grid2:
    print(gr)

grid3 = [grid[row][row] for row in range(size)] 
print("grid3: list of diagonal_left ")
print (grid3)
grid4 = [grid[row][size-(row+1)] for row in range(size)] 
print("grid4: list of diagonal_right")
print (grid4)
print("end")
