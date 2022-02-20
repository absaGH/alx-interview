#!/usr/bin/python3
"""
Rotate 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """Rotate matrix 90 degrees clockwise.
       it edit the matrix in-place.
       it is assumed matrix is 2D and not empty.
    """
    rSize = len(matrix[0])
    for i in range(rSize // 2):
        for j in range(i, rSize - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[rSize - 1 - j][i]
            matrix[rSize - 1 - j][i] = matrix[rSize - 1 - i][rSize - 1 - j]
            matrix[rSize - 1 - i][rSize - 1 - j] = matrix[j][rSize - 1 - i]
            matrix[j][rSize - 1 - i] = temp
