#!/usr/bin/python3

"""A module that rotates a matrix by 90 degrees"""


def rotate_2d_matrix(matrix):
    """returns a 90 degrees rotated matrix"""

    matrix.reverse()
    matrix_in_90_deg = []

    for idx in range(len(matrix)):
        temp_row = [element[idx] for element in matrix]
        matrix_in_90_deg.append(temp_row)

    matrix = matrix_in_90_deg

    return matrix
