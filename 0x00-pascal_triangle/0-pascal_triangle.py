#!/usr/bin/python3

"""
def_pascal_triangle: that returns a list of lists of integers representing the Pascal's triangle of n:
	- Returns an empty list if n <= 0
	- You can assume n will be always an integer
""" 

def pascal_triangle(n):
    # Check if n is less than 0, return an empty list if true
    if n < 0:
        return []

    result = [[1]]  # Triangle always starts with 1
    # Iterate through each row up to the (n - 1)th row
    for i in range(n - 1):
        # Create a temporary list with 0 padding on both sides
        temp = [0] + result[-1] + [0]
        row = []  # Initialize the current row
        # Iterate through each element of the previous row
        for j in range(len(result[-1]) + 1):
            # Calculate the value of each element in the current row
            row.append(temp[j] + temp[j + 1])
        result.append(row)  # Append the current row to the result
    return result  # Return the Pascal's triangle

