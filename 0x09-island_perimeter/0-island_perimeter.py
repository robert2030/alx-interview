#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    :param grid: List of list of integers representing the grid
    :return: Integer perimeter of the island
    """
    rows = len(grid)             # Number of rows in the grid
    cols = len(grid[0])          # Number of columns in the grid
    perimeter = 0                # Initialize the perimeter counter

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If the cell is land
                perimeter += 4   # Assume it contributes 4 edges

                # Check the cell above (if not on the first row)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

                # Check the cell to the left (if not in the first column)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

    return perimeter
