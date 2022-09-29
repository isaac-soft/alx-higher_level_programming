#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ compute the square of a matrix list"""
    new_matrix = []
    for eachList in matrix:
        new_matrix.append(list(map(lambda x: x**2, eachList)))
    return new_matrix
