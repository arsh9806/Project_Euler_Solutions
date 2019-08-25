grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

max1 = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        if j+3 < len(grid) and grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3] > max1:  #left and right
            max1 = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if j+3 < len(grid) and grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i] > max1:    #up and down
            max1 = grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]
        if i+3 < len(grid) and j+3 < len(grid) and grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3] >max1:   #Bottom right diagonal
            max1 = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if i-3 > 0 and j-3 > 0 and grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3] > max1:  #Top left diagonal
            max1 = grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3]
        if i+3 < len(grid) and j-3 > 0 and grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3] > max1:  #Bottom Left Diagonal
            max1 = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
        if i-3 > 0 and j+3 < len(grid) and grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3] > max1:  #Top Right Diagonal
            max1 = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
print(max1)