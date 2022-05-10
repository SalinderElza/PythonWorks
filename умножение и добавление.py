from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        ri, rj = range(len(self.matrix)), range(len(self.matrix[0]))
        return Matrix(
            [[self.matrix[i][j] +
              other.matrix[i][j] for j in rj] for i in ri])

    def __mul__(self, sk):
        ri, rj = range(len(self.matrix)), range(len(self.matrix[0]))
        return Matrix([[self.matrix[i][j] * sk for j in rj] for i in ri])

    __rmul__ = __mul__

    def size(self):
        return len(self.matrix), len(self.matrix[0])


exec(stdin.read())
