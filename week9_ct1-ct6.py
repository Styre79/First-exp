# 1 Класс
# Реализуйте класс Matrix. Он должен содержать:
#  - Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер.
#    Конструктор должен копировать содержимое списка списков, т. е. при изменении списков, от которых была
#    сконструирована матрица, содержимое матрицы изменяться не должно.
#  - Метод __str__, переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками
#    табуляции, а строки  —  переносами строк. После каждой строки не должно быть символа табуляции и в конце не должно
#    быть переноса строки.
#  - Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов).
#    Пример теста с участием этого метода есть в следующей задаче этой недели.
from sys import stdin


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


exec(stdin.read())

# 2 Добавить, умножить
# Добавьте в предыдущий класс следующие методы:
#      __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
#      __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
#      __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
#               Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
#    В следующем случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10.
#    В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа):
#    10 * Matrix([[0, 1], [1, 0]).
# Разумеется, данные методы не должны менять содержимое матрицы.
from sys import stdin


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
        for i in range(len(self.sumarr)):
            for j in range(len(self.sumarr[i])):
                self.sumarr[i][j] += other.arr[i][j]
        return Matrix(self.sumarr)

    def __mul__(self, other):
        self.mularr = [i[:] for i in self.arr]
        for i in range(len(self.mularr)):
            for j in range(len(self.mularr[i])):
                self.mularr[i][j] *= other
        return Matrix(self.mularr)

    __rmul__ = __mul__


exec(stdin.read())

# 3 Ошибки, транспонирование
# Добавьте в программу из предыдущей задачи класс MatrixError,
# содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
# В класс Matrix внесите следующие изменения:
#      Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных
#      размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым
#      аргументом __add__ (просто self), а matrix2  —  вторым (второй операнд для сложения).
#      Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
#      (данный метод модифицирует экземпляр класса Matrix)
#      Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.
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
        self.mularr = [i[:] for i in self.arr]
        for i in range(len(self.mularr)):
            for j in range(len(self.mularr[i])):
                self.mularr[i][j] *= other
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

# 4* Умножение
# Внесите следующие изменение в предыдущую программу:
#     Измените метод __mul__ таким образом, чтобы матрицы можно было умножать как на скаляры, так и на другие матрицы.
#     В случае, если две матрицы перемножить невозможно, то тогда выбросьте ошибку MatrixError. Первая матрице в
#     ошибке  —  это self, вторая  —  это второй операнд умножения.
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

# 5*

# 6*

