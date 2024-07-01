import os

def bomberMan(n, grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        return ['O' * len(grid[0]) for _ in grid]
        
    def explode(grid):
        new_grid = [['O' for _ in row] for row in grid]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        rows = len(grid)
        cols = len(grid[0])
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 'O':
                    new_grid[y][x] = '.'
                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < rows and 0 <= nx < cols:
                            new_grid[ny][nx] = '.'
        return [''.join(row) for row in new_grid]
    
    first_explosion = explode(grid)
    second_explosion = explode(first_explosion)
    
    return second_explosion if (n-3) % 4 else first_explosion
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
