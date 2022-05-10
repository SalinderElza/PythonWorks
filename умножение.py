from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Mtxs, other):
        self.matrix1 = Mtxs
        self.matrix2 = other


class Matrix:
    def __init__(self, l4l):
        self.Mtxs = [_.copy() for _ in l4l]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, self.Mtxs[i]))
                          for i in range(len(self.Mtxs))])

    def size(self):
        return len(self.Mtxs), len(self.Mtxs[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)
        return Matrix(list(map(
            lambda a, b: list(map(
                lambda x, y: x + y, a, b)), self.Mtxs, other.Mtxs)))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([list(map(
                lambda x: x * other, self.Mtxs[i]))
                for i in range(len(self.Mtxs))])
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            return Matrix(
                list(map(
                        lambda x: list(
                            map(
                                lambda y: sum(map(
                                    lambda z: z[0] * z[1],
                                    zip(x, y))
                                ), zip(*other.Mtxs))
                        ), zip(*Matrix.transposed(self).Mtxs))))

    __rmul__ = __mul__

    def transpose(self):
        self.Mtxs = list(map(lambda *args: list(args), *self.Mtxs))
        return Matrix(self.Mtxs)

    @staticmethod
    def transposed(M):
        return Matrix(list(map(lambda *args: list(args), *M.Mtxs)))


exec(stdin.read())
