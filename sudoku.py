import generator

def main():
    grid = generator.generate_puzzle(5)
    printGrid(grid)   
    solve(grid)
    return 0

def solve(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if generator.is_valid(grid, i, j, n):
                        grid[i][j] = n
                        solve(grid)         # Now recursive call to solve
                        grid[i][j] = 0      # backtrack
                return                      # if we've iterated through all numbers we want to quit this line
    printGrid(grid)                         

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()
    print()
    return

main()