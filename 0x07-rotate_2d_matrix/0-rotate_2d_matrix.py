#!/usr/bin/python3

"""A module that rotates a matrix by 90 degrees"""


def rotate_2d_matrix(matrix):
    """returns a 90 degrees rotated matrix"""

    copy_matrix = matrix.copy()
    matrix.clear()

    copy_matrix.reverse()

    for idx in range(len(copy_matrix)):
        temp_row = [element[idx] for element in copy_matrix]
        matrix.append(temp_row)
