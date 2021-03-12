# 1 Площадь треугольника
# Даны длины сторон треугольника. Вычислите площадь треугольника.
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('{0:.6f}'.format(s))

# 2 Сумма ряда
# По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
# Вводится целое положительное число.
n = int(input())
total = 0
while n >= 1:
    total += 1 / (n ** 2)
    n -= 1
print(total)

# 3 Дробная часть
# Дано положительное действительное число X. Выведите его дробную часть.
n = float(input())
print(n - int(n))

# 4 Цена товара
# Цена товара обозначена в рублях с точностью до копеек,
# то есть действительным числом с двумя цифрами после десятичной точки.
# Запишите в две целочисленные переменные стоимость товара в виде целого числа рублей и целого числа копеек и
# выведите их на экран. При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
price = float(input())
print(int(price), (round(price % int(price) * 100)))

# 5 Округление по российским правилам
# По российский правилам числа округляются до ближайшего целого числа,а если дробная часть числа равна 0.5,
# то число округляется вверх. Дано неотрицательное число x, округлите его по этим правилам.
# Обратите внимание, что функция round не годится для этой задачи!
n = float(input())
if n % int(n) == 0.5 and int(n) % 2 == 0:
    print(round(n) + 1)
else:
    print(round(n))

# 6 Проценты
# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
p, x, y = int(input()), int(input()), int(input())
vkop = x * 100 + y
res = vkop + (vkop * (p / 100))
print(int(res // 100), int(res % 100))

# 7 Сложные проценты
# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада через год.
# Вклад составляет X рублей Y копеек. Определите размер вклада через K лет.
# Программа получает на вход целые числа  P, X, Y, K.
# Программа должна вывести два числа: величину вклада через K лет в рублях и копейках.
# Дробное число копеек по истечение года отбрасывается.
# Перерасчет суммы вклада (с отбрасыванием дробных частей копеек) происходит ежегодно.
p, x, y, k = int(input()), int(input()), int(input()), int(input())
vkop = x * 100 + y
while k > 0:
    res = vkop + (vkop * (p / 100))
    vkop = int(res)
    k -= 1
print(int(res // 100), int(res % 100))

# 8 Схема Горнера
# Дан многочлен P(x) = a[n] xⁿ+a[n-1] xⁿ⁻¹+...+a[1] x+a[0] и число x.
# Вычислите значение этого многочлена, воспользовавшись схемой Горнера:
# P(x) = ( ... ( ( ( a[n] x + a[n-1] ) x + a[n-2] ) x + a[n-3] ) ... ) x + a[0]
# Сначала программе подается на вход целое неотрицательное число n ≤ 20, затем действительное число x,
# затем следует n+1 вещественных чисел — коэффициенты многочлена от старшего к младшему.
n = int(input())
x = float(input())
px = float(input())
while n != 0:
    a = float(input())
    px = px * x + a
    n -= 1
print(px)

# 9 Стандартное отклонение
# Дана последовательность натуральных чисел x₁, x₂ ..., xn. Стандартным отклонением называется величина
# σ=sqrt(((x₁-s)²+(x₂-s)²+…+(xn-s)²) / (n-1))
# где s = ((x₁+x₂+…+xn) / n) — среднее арифметическое последовательности, а sqrt - квадратный корень.
# Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
import math

x = int(input())
sx = 0
sx2 = 0
n = 0
while x != 0:
    n += 1
    sx += x
    sx2 += x ** 2
    x = int(input())
print(math.sqrt((sx2 - (sx ** 2) / n) / (n - 1)))
# формула в print нагуглена на форуме, я не математик :(

# 10 Квадратное уравнение - 1
# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
# Если уравнение имеет два корня, выведите два корня в порядке возрастания, если один корень — выведите одно число,
# если нет корней — не выводите ничего.
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    elif x2 < x1:
        print(x2, x1)
    else:
        print(x1)

# 11 Квадратное уравнение - 2
# Даны произвольные действительные коэффициенты a, b, c. Решите уравнение ax²+bx+c=0.
# Если данное уравнение не имеет корней, выведите число 0. Если уравнение имеет один корень, выведите число 1,
# а затем этот корень. Если уравнение имеет два корня, выведите число 2, а затем два корня в порядке возрастания.
# Если уравнение имеет бесконечно много корней, выведите число 3.
a, b, c = float(input()), float(input()), float(input())
if a != 0:
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if x1 == x2:
            print(1, x1)
        else:
            print(2, min(x1, x2), max(x1, x2))
    else:
        print(0)
elif b == 0:
    if c == 0:
        print(3)
    else:
        print(0)
else:
    x1 = -c / b
    print(1, x1)

# 12 Система линейных уравнений - 1
# Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой системы.
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
x = (f * b - d * e) / (c * b - d * a)
y = (f * a - c * e) / (a * d - c * b)
print(x, y)

# 13 Система линейных уравнений - 2
# Вводятся 6 чисел a, b, c, d, e, f — коэффициенты уравнений.
# Вывод программы зависит от вида решения этой системы.
# Если система не имеет решений, то программа должна вывести единственное число 0.
# Если система имеет бесконечно много решений, каждое из которых имеет вид y=px+q, то программа должна вывести число 1,
# а затем значения p и q.
# Если система имеет единственное решение (x₀,y₀), то программа должна вывести число 2, а затем значения x₀ и y₀.
# Если система имеет бесконечно много решений вида x=x₀, y — любое, то программа должна вывести число 3,
# а затем значение x₀.
# Если система имеет бесконечно много решений вида y=y₀, x — любое, то программа должна вывести число 4,
# а затем значение y₀.
# Если любая пара чисел (x,y) является решением, то программа должна вывести число 5.
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == b == c == d == e == f == 0:
    print(5)
elif a * d - b * c != 0:
    x = (f * b - d * e) / (c * b - d * a)
    y = (f * a - c * e) / (a * d - c * b)
    print(2, x, y)
elif (b == d == 0) and (a != 0 and c != 0 and e != 0 and f != 0) \
        and (e / a == f / c):
    print(3, e / a)
elif (a == c == 0) and (b != 0 and d != 0 and e != 0 and f != 0) \
        and (e / a == f / c):
    print(3, e / a)
else:
    print("Ok")
# забил!!! пока не работает!!!

# 14 Делаем срезы
# Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.
st = input()
print(st[2])
print(st[-2])
print(st[:5])
print(st[:-2])
print(st[::2])
print(st[1::2])
print(st[::-1])
print(st[-1::-2])
print(len(st))

# 15 Первое и последнее вхождение
# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.
# При решении этой задачи нельзя использовать метод count и циклы.
st = input()
if st.find('f') != -1:
    if (len(st) - 1 - st[::-1].find('f')) == st.find('f'):  # находим 1-е вхождение в инверсной строке, вычисляем
        print(st.find('f'))  # его инднекс в исходной строке и сравниваем с индексом
    else:  # 1-го вхождения в исходной строке
        print(st.find('f'), len(st) - 1 - st[::-1].find('f'))

# 16 Удаление фрагмента
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,а также все символы, находящиеся между ними.
st = input()
print(st[:st.find('h')] + st[(len(st) - st[::-1].find('h'))::])

# 17 Дублирование фрагмента
# Дана строка, в которой буква h встречается как минимум два раза. Выведите измененную строку:
# повторите последовательность символов, заключенную между первым и последним появлением буквы h два раза
# (сами буквы h не входят в повторяемый фрагмент, т. е. их повторять не надо).
st = input()
fh = st.find('h')  # first entry 'h'
lh = len(st) - 1 - st[::-1].find('h')  # last entry 'h'
print(st[:fh + 1] + st[fh + 1:lh] * 2 + st[lh:])

# 18 Второе вхождение
# Дана строка. Найдите в этой строке второе вхождение буквы f и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1,
# а если не встречается ни разу, выведите число -2. При решении этой задачи нельзя использовать метод count.
st = input()
index = 0
entry_count = 0
while st.find('f', index) != -1:
    index = st.find('f', index) + 1
    entry_count += 1
    if entry_count == 2:
        print(index - 1)
        break
if entry_count == 1:
    print(-1)
elif entry_count == 0:
    print(-2)

# 19 Переставить два слова
# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.
st = input()
print(st[st.find(' ') + 1:] + ' ' + st[:st.find(' ')])

# 20 Количество слов
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
st = input()
print(st.count(' ') + 1)

# 21 Замена подстроки
# Дана строка. Замените в этой строке все цифры 1 на слово one.
st = input()
print(st.replace('1', 'one'))

# 22 Удаление символа
# Дана строка. Удалите из этой строки все символы @.
st = input()
print(st.replace('@', ''))

# 23 Замена внутри фрагмента
# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
st = input()
before_first_entry = st[:st.find('h') + 1]
after_last_entry = st[st.rfind('h'):]
h_to_H = st[st.find('h') + 1:st.rfind('h')].replace('h', 'H')
print(before_first_entry + h_to_H + after_last_entry)

# 24 Вставка символов
# Дана строка. Получите новую строку, вставив между каждыми двумя символами исходной строки символ *.
# Выведите полученную строку.
st = input()
i = 1
print(st[0], end='')
while i < len(st):
    print('*', end='')
    print(st[i], end='')
    i += 1

# 25 Удалить каждый третий символ
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.Символы строки нумеруются, начиная с нуля.
st = input()
i = 0
res = ''
while i < len(st):
    if i % 3 != 0:
        res = res + st[i]
    i += 1
print(res)