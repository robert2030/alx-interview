#!/usr/bin/python3
# Pascal's Triangle
def pascal_triangle(n):
    """
    Print Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return
    
    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        row = [1]  # First element is always 1
        # Fill in the middle values using the sum of adjacent numbers from the previous row
        row += [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)]
        row.append(1)  # Last element is always 1
        triangle.append(row)
    
    # Print the triangle
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
