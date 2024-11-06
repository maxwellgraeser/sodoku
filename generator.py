import random

# Checks if a number can be placed at the specified row and column
def is_valid(grid, row, col, num):
    # Check the row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

# Fills the grid completely with a valid Sudoku solution
def fill_grid(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if fill_grid(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Finds an empty location in the grid (represented by 0)
def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

# Checks if the grid has a unique solution
def has_unique_solution(grid):

    solutions_found = [0]

    def backtrack(grid):
        empty = find_empty_location(grid)
        if not empty:
            solutions_found[0] += 1
            return solutions_found[0] == 1  # Stop searching if a second solution is found

        row, col = empty
        for num in range(1, 10):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                if backtrack(grid):
                    if solutions_found[0] > 1:
                        return False  # Exit if more than one solution is found
                grid[row][col] = 0  # Backtrack

        return solutions_found[0] == 1

    backtrack(grid)
    return solutions_found[0] == 1

# Generates a Sudoku puzzle by removing numbers from a filled grid
# Difficulty is an int between 1-5
def generate_puzzle(difficulty):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)

    # Adjust the number of cells to remove based on difficulty
    attempts = 5 * difficulty
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        
        # Temporarily remove cell value
        backup = grid[row][col]
        grid[row][col] = 0

        # Check if the grid still has a unique solution after removal
        if not has_unique_solution(grid):
            grid[row][col] = backup  # Restore if puzzle becomes unsolvable
        attempts -= 1

    return grid
