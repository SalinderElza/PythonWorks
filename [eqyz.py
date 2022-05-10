from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other
        self.matrixError = "\nThe matrix:\n" + str(self.matrix1) +\
                           "\ndoes not match the size of the matrix:\n" +\
                           str(self.matrix2) + "\n"


class Matrix:
    __cc = 0

    @property
    def cnt(self):
        return Matrix.__cc

    @cnt.setter
    def cnt(self, newStatus):
        if newStatus == Matrix.__cc + 1:
            Matrix.__cc = newStatus

    @staticmethod
    def transposed(self):
        myTuple = tuple(zip(*self.rList))
        outList = []
        for i in range(len(myTuple)):
            outList.append(list(myTuple[i]))
        return Matrix(outList)

    @staticmethod
    def determinator(m):
        if m.size()[0] == 2:
            return m.rList[0][0] * m.rList[1][1] - \
                   m.rList[0][1] * m.rList[1][0]
        elif m.size()[0] == 3:
            return \
                m.rList[0][0] * m.rList[1][1] * m.rList[2][2] \
                + m.rList[2][0] * m.rList[0][1] * m.rList[1][2] \
                + m.rList[1][0] * m.rList[2][1] * m.rList[0][2] \
                - m.rList[2][0] * m.rList[1][1] * m.rList[0][2] \
                - m.rList[0][0] * m.rList[2][1] * m.rList[1][2] \
                - m.rList[1][0] * m.rList[0][1] * m.rList[2][2]
        else:
            raise Exception("\nMatrix's range more than 3.\n")

    def __init__(self, rList):
        self.cnt += 1
        self.rList = []
        for i in range(len(rList)):
            self.rList.append(rList[i][:])

    def __str__(self):
        strOut = ""
        for i in range(len(self.rList)):
            strOut += "\t".join(map(str, self.rList[i])) + "\n"
        return strOut[:-1]

    def __testMatrix(self, other, op):
        testMatrix = True
        if op == "add" or op == "sub":
            if len(self.rList) == len(other.rList):
                for i in range(len(self.rList)):
                    if len(self.rList[i]) != len(other.rList[i]):
                        testMatrix = False
                        raise MatrixError(self.rList, other.rList)
            else:
                testMatrix = False
                raise MatrixError(self, other)
            return testMatrix
        if op == "mul" or op == "rmul":
            if self.size()[1] != other.size()[0]:
                testMatrix = False
                raise MatrixError(self, other)
            return testMatrix

    def __add__(self, other):
        outList = []
        if isinstance(other, Matrix) and self.__testMatrix(other, "add"):
            for i in range(len(self.rList)):
                outList.append([])
                for ii in range(len(self.rList[i])):
                    outList[i].append(other.rList[i][ii] + self.rList[i][ii])
            return Matrix(outList)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.rList)):
                outList.append([])
                for ii in range(len(self.rList[i])):
                    outList[i].append(self.rList[i][ii] + other)
            return Matrix(outList)

    def __sub__(self, other):
        outList = []
        if isinstance(other, Matrix) and self.__testMatrix(other, "sub"):
            for i in range(len(self.rList)):
                outList.append([])
                for ii in range(len(self.rList[i])):
                    outList[i].append(self.rList[i][ii] - other.rList[i][ii])
            return Matrix(outList)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.rList)):
                outList.append([])
                for ii in range(len(self.rList[i])):
                    outList[i].append(self.rList[i][ii] - other)
            return Matrix(outList)

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.__testMatrix(other, "mul"):
            return Matrix(
                list(map(
                    lambda x: list(
                        map(
                            lambda y: sum(map(
                                lambda z: z[0] * z[1],
                                zip(x, y))
                            ),
                            zip(*other.rList))),
                    zip(*Matrix.transposed(self).rList))
                )
            )
        if isinstance(other, int) or isinstance(other, float):
            outList = []
            for i in range(len(self.rList)):
                outList.append([])
                for ii in range(len(self.rList[i])):
                    outList[i].append(self.rList[i][ii] * other)
            return Matrix(outList)

    __rmul__ = __mul__

    def size(self):
        return len(self.rList), len(self.rList[0])

    def transpose(self):
        myTuple = tuple(zip(*self.rList))
        self.rList = []
        for i in range(len(myTuple)):
            self.rList.append(list(myTuple[i]))
        return Matrix(self.rList)

    def solve(self, vector):
        if self.size()[1] != self.size()[0]:
            raise Exception("\nThe Matrix is not square.\n")
        elif self.size()[1] != len(vector):
            raise Exception("\nThe Matrix and vector have different length.\n")
        outList = []
        for i in range(len(vector)):
            m = Matrix(self.rList)
            for ii in range(len(vector)):
                m.rList[ii][i] = vector[ii]
            outList.append(Matrix.determinator(m))
        return list(map(lambda x: x / Matrix.determinator(self), outList))


class SquareMatrix(Matrix):
    def __mul__(self, other):
        return SquareMatrix(super().__mul__(other).rList)

    def __pow__(self, p):
        if p in [0, 1]:
            return self
        elif p == 2:
            return self * self
        if p % 2 != 0:
            return self * (self ** (p - 1))
        else:
            return (self * self) ** (p // 2)


exec(stdin.read())
