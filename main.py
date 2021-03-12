# for commit changes
# this comment

from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, in_list):
        self.arr = [i[:] for i in in_list]

    def __str__(self):
        self.str_arr = ''
        for i in self.arr:
            self.str_arr += '\t'.join(map(str, i))
            self.str_arr += '\n'
        self.str_arr = self.str_arr.rstrip()
        return self.str_arr

    def size(self):
        return len(self.arr), len(self.arr[0])

    def __add__(self, other):
        self.sumarr = [i[:] for i in self.arr]
        if len(self.sumarr) != len(other.arr):
            raise MatrixError(self, other)
        for i in range(len(self.sumarr)):
            if len(self.sumarr[i]) != len(other.arr[i]):
                raise MatrixError(self, other)
            for j in range(len(self.sumarr[i])):
                self.sumarr[i][j] += other.arr[i][j]
        return Matrix(self.sumarr)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.mularr = [i[:] for i in self.arr]
            for i in range(len(self.mularr)):
                for j in range(len(self.mularr[i])):
                    self.mularr[i][j] *= other
        elif isinstance(other, Matrix) \
                and len(self.arr[0]) == len(other.arr):
            self.mularr = [[0 for i in range(len(other.arr[0]))]
                           for j in range(len(self.arr))]
            for i in range(len(self.mularr)):
                for j in range(len(self.mularr[0])):
                    for k in range(len(self.arr[0])):
                        self.mularr[i][j] += self.arr[i][k] * other.arr[k][j]
        else:
            raise MatrixError(self, other)
        return Matrix(self.mularr)

    __rmul__ = __mul__

    def transpose(self):
        self.transarr = [[self.arr[j][i] for j in range(len(self.arr))]
                         for i in range(len(self.arr[0]))]
        self.arr = self.transarr
        return Matrix(self.arr)

    @staticmethod
    def transposed(self):
        self.transarr = [[self.arr[j][i] for j in range(len(self.arr))]
                         for i in range(len(self.arr[0]))]
        return Matrix(self.transarr)


exec(stdin.read())
