
def minesweeper(grid):
# firstly Intializing the rows and columns
row_num =len(grid)
column_num =len(grid[0])
#========New grid is created=======
new_grid = [[0]*column_num for _ in range(row_num)]
hash_count=0
# Outer loop For rows
for count_row,row in enumerate(grid):
# Inner loop For Columns
   for  count_column, col in enumerate(row):
      if col == "#":
         new_grid[count_row][count_column] ="#"
      else:
        if count_row>=0 and count_row< len(grid)-1 :
           if grid[count_row+1][count_column] == "#":
              hash_count += 1
        if  count_row> 0 and count_row<= len(grid)-1 :    
           if grid[count_row -1][count_column] == "#":
              hash_count += 1
        if count_column >= 0 and count_column < len(row)-1:
           if row[count_column+1] == "#":
              hash_count += 1                   
        if count_column > 0 and count_column <= len(row)-1:       
            if row[count_column-1] == "#":
               hash_count += 1
# New gris is displayed
for row in minesweeper(grid):
    print(row)              
