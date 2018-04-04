# Implementing a region size counter with recursion
# Trick is to replaced counted points with 0s

def getBiggestRegion(grid):
    r = len(grid)
    c = len(grid[0])

    max_count = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                cnt = process_region(grid,i,j,r,c)
                if cnt > max_count:
                    max_count = cnt

    return max_count

def process_region(grid,i_s,j_s,r,c):
    cnt = 1
    grid[i_s][j_s] = 0
    expcomb1 = [1,1,1,0,0,-1,-1,-1]
    expcomb2 = [1,0,-1,1,-1,1,0,-1]
    for e_x,e_y in zip(expcomb1,expcomb2):
        # can we explore?
        next_x = i_s + e_x
        next_y = j_s + e_y
        if next_x >= 0 and next_x < r and next_y >= 0 and next_y < c:
            i_e = i_s + e_x
            j_e = j_s + e_y
            if grid[i_e][j_e] == 1:
                cnt += process_region(grid,i_e,j_e,r,c)
    return cnt



n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
