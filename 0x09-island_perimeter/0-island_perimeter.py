#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ return the perimeter of the island described in grid """
    total_perimeter = 0

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            # Check if element is land or sea
            if (element == 0):
                continue

            # Left check
            if (j != 0 and row[j - 1] == 0):
                total_perimeter += 1
            if (j == 0):
                # left edge case
                total_perimeter += 1

            # Right check
            if (j != len(row) - 1 and row[j + 1] == 0):
                total_perimeter += 1
            if (j == len(row) - 1):
                # right edge case
                total_perimeter += 1

            # Upper check
            if (i != 0 and grid[i - 1][j] == 0):
                total_perimeter += 1
            if (i == 0):
                # top edge case
                total_perimeter += 1

            # Bottom Check
            if (i != len(grid) - 1 and grid[i + 1][j] == 0):
                total_perimeter += 1
            if (i == len(grid) - 1):
                # bottom edge case
                total_perimeter += 1

    return total_perimeter
