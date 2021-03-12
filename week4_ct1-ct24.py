# 1 Минимум 4 чисел
# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел, которая не содержит инструкции if,
# а использует стандартную функцию min от двух чисел. Считайте четыре целых числа и выведите их минимум.
def min4(a, b, c, d):
    return min(min(a, b), min(c, d))


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))

# 2 Длина отрезка
# Даны четыре действительных числа: x₁, y₁, x₂, y₂. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками (x₁,y₁) и (x₂,y₂).
# Считайте четыре действительных числа и выведите результат работы этой функции.
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
print(distance(x1, y1, x2, y2))

# 3 Периметр треугольника
# Напишите функцию, вычисляющую длину отрезка по координатам его концов. С помощью этой функции напишите программу,
# вычисляющую периметр треугольника по координатам трех его вершин.
# На вход программе подается 6 целых чисел — координат x₁, y₁, x₂, y₂, x₃, y₃ вершин треугольника.
# Все числа по модулю не превосходят 30 000. Выведите значение периметра с точностью до 6 знаков после десятичной точки.
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def triangle_perimetr(ab, ac, bc):
    return ab + ac + bc


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
print('{0:.6f}'.format(triangle_perimetr(distance(x1, y1, x2, y2),
                                         distance(x1, y1, x3, y3),
                                         distance(x2, y2, x3, y3))))

# 4 Принадлежит ли точка квадрату - 1
# Даны два действительных числа x и y. Проверьте, принадлежит ли точка с координатами (x,y) квадрату
# c координатами вершин ((-1;1)(1;1)(1;-1)(-1;-1))(включая его границу).
# Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInSquare(x, y), возвращающую True, если точка принадлежит квадрату и False,
# если не принадлежит. Основная программа должна считать координаты точки, вызвать функцию IsPointInSquare и
# в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInSquare не должна содержать инструкцию if.
def IsPointInSquare(x, y):
    return (-1 <= x <= 1) and (-1 <= y <= 1)


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

# 5 Принадлежит ли точка квадрату - 2
# Даны два действительных числа x и y. Проверьте, принадлежит ли точка с координатами(x,y) квадрату
# c координатами вершин ((0;1)(1;0)(0;-1)(-1;0))(включая его границу). Если точка принадлежит квадрату,
# выведите слово YES,иначе выведите слово NO. На рисунке сетка проведена с шагом 1.
# Решение должно содержать функцию IsPointInSquare(x, y), возвращающую True, если точка принадлежит квадрату и False,
# если не принадлежит. Основная программа должна считать координаты точки, вызвать функцию IsPointInSquare и
# в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInSquare не должна содержать инструкцию if.
def IsPointInSquare(x, y):
    return (abs(x) <= (1 - abs(y))) and (abs(y) <= (1 - abs(x)))


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

# 6 Принадлежит ли точка кругу
# Даны пять действительных чисел: x, y, xc, yc, r.
# Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
# Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r), возвращающую True,
# если точка принадлежит кругу и False, если не принадлежит.
# Основная программа должна считать координаты точки, вызвать функцию IsPointInCircle и в зависимости от возвращенного
# значения вывести на экран необходимое сообщение. Функция IsPointInCircle не должна содержать инструкцию if.
def IsPointInCircle(x, y, xc, yc, r):
    return (y - yc) ** 2 + (x - xc) ** 2 <= r ** 2


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')

# 7 Принадлежит ли точка области
# Проверьте, принадлежит ли точка данной закрашенной области:
# picture(w4ct7.png) in folder
# Если точка принадлежит области (область включает границы), выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInArea(x, y), возвращающую True, если точка принадлежит области и False,
# если не принадлежит. Основная программа должна считать координаты точки, вызвать функцию IsPointInArea и
# в зависимости от возвращенного значения вывести на экран необходимое сообщение. Функция IsPointInArea не должна
# содержать инструкцию if.
def IsPointInCircle(x, y, xc, yc, r):
    return (y - yc) ** 2 + (x - xc) ** 2 <= r ** 2


def IsPointNotInCircle(x, y, xc, yc, r):
    return (y - yc) ** 2 + (x - xc) ** 2 >= r ** 2


def IsPointBetweenTwoLinesYPlus(x, y):
    return (x >= -y) and (x <= ((y - 2) / 2))


def IsPointBetweenTwoLinesYMinus(x, y):
    return (x <= -y) and (x >= ((y - 2) / 2))


def IsPointInArea(x, y):
    return IsPointInCircle(x, y, xc, yc, r) and \
           IsPointBetweenTwoLinesYPlus(x, y)


x, y = float(input()), float(input())
xc, yc, r = -1, 1, 2
if (y >= 0 and IsPointInArea(x, y)) or \
        (y < 0 and IsPointBetweenTwoLinesYMinus(x, y) and
         IsPointNotInCircle(x, y, xc, yc, r)):
    print('YES')
else:
    print('NO')

# 8 Напишите функцию xor(x, y)  реализующую функцию "Исключающее ИЛИ" двух логических переменных x и y.
# Функция xor должна возвращать True, если ровно один из ее аргументов x или y, но не оба одновременно равны True.
# Вводится 2 числа - x и y (x и y равны 0 или 1, 0 соответствует значению False, 1 соответствует значению True).
def xor(x, y):
    return int(x + y == 1)


x, y = int(input()), int(input())
print(xor(x, y))

# 9 Минимальный делитель числа
# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1. Решение оформите в виде функции
# MinDivisor(n). Алгоритм должен иметь сложность порядка корня квадратного из n.
# Указание. Если у числа n нет делителя не превосходящего корня из n,
# то число n — простое и ответом будет само число n. А у всех составных чисел обязательно есть делители,
# отличные от единицы и не превосходящие корня из n.
def MinDivisor(n):
    min_div = 2
    if n % 2 == 0:
        return min_div
    else:
        min_div += 1
        while min_div <= n ** 0.5:
            if n % min_div == 0:
                return min_div
            min_div += 2
        return n


n = int(input())
print(MinDivisor(n))

# 10 Проверка числа на простоту
# Дано натуральное число n>1. Проверьте, является ли оно простым. Программа должна вывести слово YES,
# если число простое и NO, если число составное. Решение оформите в виде функции IsPrime(n), которая возвращает True
# для простых чисел и False для составных чисел. Программа должна иметь сложность O(корень из n): количество действий
# в программе должно быть пропорционально квадратному корню из n (иначе говоря, при увеличении входного числа в k раз,
# время выполнения программы должно увеличиваться примерно в корень из k раз).
def MinDivisor(n):
    min_div = 2
    if n % 2 == 0:
        return min_div
    else:
        min_div += 1
        while min_div <= n ** 0.5:
            if n % min_div == 0:
                return min_div
            min_div += 2
        return n


def IsPrime(n):
    return MinDivisor(n) == n


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')

# 11 Возведение в степень
# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите aⁿ, не используя циклы и стандартную функцию pow, но используя рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).
# Вводятся действительное положительное число a и целое неотрицательное число n.
def power(a, n):
    if n == 0:
        a = 1
        return a
    return a * power(a, n - 1)


a, n = float(input()), int(input())
print(power(a, n))

# 12 Отрицательная степень
# Дано действительное положительное число a и целоe число n. Вычислите aⁿ.
# Решение оформите в виде функции power(a, n). Стандартной функцией возведения в степерь пользоваться нельзя.
# Вводится действительное положительное число a и целоe число n.
def power(a, n):
    res = 1
    pow_counter = abs(n)
    while pow_counter > 0:
        res *= a
        pow_counter -= 1
    if n < 0:
        res = 1 / res
    return res


a, n = float(input()), int(input())
print(power(a, n))

# 13 Сложение без сложения
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Вводятся два удовлетворяющих условию задачи числа. Числа не превышают 900.
def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)


a, b = int(input()), int(input())
print(sum(a, b))

# 14 Быстрое возведение в степень
# Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно воспользоваться следующими
# рекуррентными соотношениями: aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n.
# Реализуйте алгоритм быстрого возведения в степень. Если вы все сделаете правильно,то
# сложность вашего алгоритма будет O(logn). Вводится действительное число a и целое неотрицательное число n.
def fast_pow(a, n):
    if n == 0:
        a = 1
        return a
    if n % 2 == 0:
        return fast_pow(a * a, n / 2)
    return a * fast_pow(a, n - 1)


a, n = float(input()), int(input())
print(fast_pow(a, n))

# 15 Алгоритм Евклида
# Для быстрого вычисления наибольшего общего делителя двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).
# Вводится два целых положительных числа.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = int(input()), int(input())
print(gcd(a, b))

# 16 Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
# Вводятся два натуральных числа.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ReduceFraction(n, m):
    return int(n / gcd(n, m)), int(m / gcd(n, m))


n, m = int(input()), int(input())
print(*ReduceFraction(n, m))

# 17 Числа Фибоначчи
# Напишите функцию phib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
# В этой задаче нельзя использовать циклы - используйте рекурсию.
def phib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return phib(n - 2) + phib(n - 1)


n = int(input())
print(phib(n))

# 18 Число сочетаний
# По данным целым числам n и k  (0≤k≤n) вычислите C из n по k. Решение оформите в виде функции C(n, k).
# Для решения используйте рекуррентное соотношение: (Cn)**k=(Cn-1)**k+(Cn-1)**(k-1) И равенства:
# С(n, 1)=n и C(n, n)=1
def Cnk(n, k):
    if k == 1:
        return n
    if k == n or k == 0:
        return 1
    return (Cnk(n - 1, k) + Cnk(n - 1, k - 1))


n, k = int(input()), int(input())
print(Cnk(n, k))

# 19 Сумма последовательности
# Дана последовательность чисел, завершающаяся числом 0. Найдите сумму всех этих чисел, не используя цикл.
def sum(res=0):
    n = int(input())
    if n == 0:
        return res
    res += n
    return sum(res)


print(sum())

# 20 Разворот последовательности
# Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
# При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных.Рекурсия вам поможет.
def revseq():
    n = int(input())
    if n != 0:
        revseq()
    print(n)


revseq()

# 21 Ханойские башни
# Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
# На стержень 1 надета пирамидка из n дисков различного диаметра в порядке убывания диаметра
# (снизу находится самый большой диск, а сверху — самый маленький). Диски можно перекладывать с одного стержня
# на другой по одному, при этом диск нельзя класть на диск меньшего диаметра. Необходимо переложить всю пирамидку
# со стержня 1 на стержень 3 за минимальное число перекладываний. Напишите программу, которая решает головоломку;
# для данного числа дисков n печатает последовательность перекладываний в формате a b c,
# где a — номер перекладываемого диска, b — номер стержня с которого снимается данный диск,
# c — номер стержня на который надевается данный диск.
# Например, строка 1 2 3 означает перемещение диска номер 1 со стержня 2 на стержень 3.
# В одной строке печатается одна команда. Диски пронумерованы числами от 1 до n в порядке возрастания диаметров.
# Программа должна вывести минимальный (по количеству произведенных операций)
# способ перекладывания пирамидки из данного числа дисков.
# Напишите функцию move (n, x, y), которая печатает последовательность перекладываний дисков для перемещения
# пирамидки высоты n со стержня номер x на стержень номер y.
# def move(n, x, y):
#     if n == 1:
#         print(1, x, y)
#     else:
#         move(n - 1, x, 6 - x - y)
#         print(n, x, y)
#         move(n - 1, 6 - x - y, y)
#
#
# n = int(input())
# move(n, 1, 3)
# НЕ АСИЛИЛ!!! Решение с форума!!!!

# 22 Теорема Лагранжа
# Теорема Лагранжа утверждает, что любое натуральное число можно представить в виде суммы четырех точных квадратов.
# По данному числу n найдите такое представление: напечатайте от 1 до 4 натуральных чисел,
# квадраты которых дают в сумме данное число.
# Программа получает на вход одно натуральное число n < 10000.
# Программа должна вывести от 1 до 4 натуральных чисел, квадраты которых дают в сумме данное число.
# def lagrange(n):
#     sqrtN = n ** 0.5
#     print(int(sqrtN), end=' ')
#     if int(sqrtN) ** 2 == n:
#         return
#     n -= int(sqrtN) ** 2
#     lagrange(n)
#
#
# n = int(input())
# lagrange(n)
# Решение в "лоб", не проходит для некоторых чисел(23, 32, 48, 167, 192 ...). Необходимо, учесть кол-во шагов,
# если больше 4-х, то возврат в начало и -1 от n**0.5

# 23 Сумма кубов
# Напишите программу, которая представляет переданное натуральное число в виде суммы не более чем 7 кубов
# других натуральных чисел.
# Входная строка содержит целое число N, которое нужно представить в виде суммы кубов.
# Программа должна вывести любое разложение переданного ей числа в виде суммы не более чем 7 кубов других
# натуральных чисел. Если такое разложение невозможно, программа должна вывести число 0.

# на математику ЗАБИЛ!!!

# 24 Только квадраты
# Напишите программу, которая выбирает из полученной последовательности квадраты целых чисел выводит их
# в обратном порядке. Использовать массив для хранения последовательности не разрешается.
# Во входных строках записаны целые числа, по одному в каждой строке. В последней строке записано число 0.
# Программа должна вывести элементы полученной последовательности, которые представляют собой квадраты целых чисел,
# в обратном порядке в одну строчку, разделив их пробелами. Если таких нет, программа должна вывести число 0.
def revseqpow2():
    global Flag
    n = int(input())
    if n != 0:
        revseqpow2()

    if n != 0 and int(n ** 0.5) ** 2 == n:
        print(str(n), end=' ')
        Flag = False


Flag = True
revseqpow2()
if Flag:
    print(0)