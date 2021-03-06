# 1 Количество различных чисел
# Дан список чисел, который может содержать до 100000 чисел.Определите, сколько в нем встречается различных чисел.
print(len(set(map(int, input().split()))))

# 2 Количество слов в тексте
# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки. Определите, сколько различных слов содержится в этом тексте.
print(
    len(
        set(
            open('input.txt', 'r', encoding='utf-8').read().split()
            )
        )
    )

# 3 Наименьший нечетный
# Выведите значение наименьшего нечетного элемента списка,гарантируется,что хотя бы один нечётный элемент в списке есть.
# Вводится список чисел. Все числа списка находятся на одной строке.
import functools

print(
    functools.reduce(
        min, filter(
            lambda x: x % 2, map(   # редьюс не нужен!!!
                int, input().split()
                                )
                    )
                    )
    )

# 4 Ноль или не ноль
# Проверьте, есть ли среди данных N чисел нули. Вводится число N, а затем N чисел.
# Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в противном случае.
import sys

print(not all(map(int, sys.stdin.read().split())))

# 5 Произведение пятых степеней
# На вход подаётся последовательность натуральных чисел длины n≤1000.
# Посчитайте произведение пятых степеней чисел в последовательности.
import functools
print(functools.reduce(lambda x, y: x*(y**5), map(int, input().split()), 1))

# 6 XOR
# Булева функция XOR (сложение по модулю два) задаётся следующей таблицей истинности:
# xor(0,0)=0
# xor(0,1)=1
# xor(1,0)=1
# xor(1,1)=0
# На вход подаются две последовательности (a₁,…,an) и (b₁,…,bn) из 0 и 1.
# Вычислите последовательность из (c₁,…,cn), где каждая cᵢ=xor(aᵢ,bᵢ).
# На вход подаются две строки из 0 и 1, разделённых пробелами.
# Первая строка  —  это последовательность (a₁,…,an).
# Вторая строка  —  это последовательность (b₁,…,bn).
# Выведите последовательность (c₁,…,cn), разделяя каждый элемент пробелом
# Для решения задачи можете использовать функцию zip.
print(
    *map(
        lambda x: int(x[0] != x[1]),
        zip(map(int, input().split()),
            map(int, input().split()))))

# 7* Частичные суммы
# По заданной последовательности:
# (a₁,…,an) посчитайте последовательность частичных сумм: (S₁,…,Sn), где Sk=a₁+a₂+…+ak.
# Вводится последовательность чисел (a₁,…,an), разделённая пробелами.
# Выведите последовательность (S₁,…,Sn), разделяя числа пробелами.
# Для решения задачи можно воспользоваться функцией accumulate из модуля itertools.
import itertools
print(*itertools.accumulate(map(int, input().split())))

# 8* Факториалы
# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов: 0!,1!,2!,…,n!
# Вводится число n. Выведите последовательность факториалов, разделяя числа пробелами
import itertools

print(1, *itertools.accumulate(range(1, int(input()) + 1), lambda x, y: x * y))

# 9* Все перестановки заданной длины
# По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.
# Задано 1 число: N (0<N<10). Необходимо вывести все перестановки чисел от 1 до N в лексикографическом порядке.
# Перестановки выводятся по одной в строке, числа в перестановке выводятся без пробелов.
import itertools

print(*map(     # Мьсе знают толк в извращениях. Списал с форума!!!
    lambda x: ''.join(x), map(
        list, itertools.permutations(
            map(str, range(1, int(input()) + 1))))), sep='\n')

# 10* XOR - 2
# XOR для произвольного числа аргументов определяется следующим образом:
# xor(a₁,a₂,…,an)= xor(a₁, xor(a₂, xor(a₃,… xor(an))…)
# XOR от n последовательностей A₁,…,An (Aᵢ=Aᵢ₁,…,Aᵢk) равных длин k  —  это последовательность C=xor(A₁,…,An),такая,что:
# cᵢ=xor(A₁ᵢ,…Anᵢ) Посчитайте XOR от n последовательностей равной длины k.
# На первой строке записано число 2≤n≤1000  —  количество последовательностей.
# На последующих n строках записаны последовательности A₁,…,An из 0 и 1, разделённых пробелами равной длины 1≤k≤1000.
# Выведите последовательность C=xor(A₁,…,An), разделяя числа последовательности пробелами.

# # Мьсе знают толк в извращениях часть вторая. Даже нет желания брать решение с форума!!!

# 11* Простые числа
# Выведите все простые на отрезке [2;n]. Выведите все простые числа из отрезка [2,n] в порядке возрастания
# Напомним, что проверить число на то, простое ли оно можно за количество операций порядка √(N).
# Также напомним, что функция math.sqrt работает значительно быстрее, чем (x ** 1/2).
from math import sqrt
print(*filter(          # Мьсе знают толк в извращениях. Списал с форума!!!
    lambda x: all(map(
        lambda y: x % y, range(2, round(sqrt(x)) + 1))), range(2, int(input()) + 1)))

# 12* Ставки
# Перед началом тараканьих бегов всем болельщикам было предложено сделать по две ставки на результаты бегов.
# Каждая ставка имеет вид "Таракан №A придет раньше, чем таракан №B". Организаторы бегов решили выяснить, могут ли
# тараканы прийти в таком порядке, чтобы у каждого болельщика сыграла ровно одна ставка из двух (то есть чтобы ровно
# одно из двух утверждений каждого болельщика оказалось верным). Считается, что никакие два таракана не могут прийти
# к финишу одновременно.
# В первой строке входных данных содержатся два разделенных пробелом натуральных числа: число K, не превосходящее 10,
# - количество тараканов и число N, не превосходящее 100, - количество болельщиков. Все тараканы пронумерованы числами
# от 1 до K. Каждая из следующих N строк содержит 4 натуральных числа A, B, C, D, не превосходящих K,
# разделенных пробелами. Они соответствуют ставкам болельщика "Таракан №A придет раньше, чем таракан №B" и
# "Таракан №C придет раньше, чем таракан №D".
# Если завершить бега так, чтобы у каждого из болельщиков сыграла ровно одна из двух ставок, можно, то следует вывести
# номера тараканов в том порядке, в котором они окажутся в итоговой таблице результатов (сначала номер таракана,
# пришедшего первым, затем номер таракана, пришедшего вторым и т. д.) в одну строку через пробел. Если таких вариантов
# несколько, выведите любой из них. Если требуемого результата добиться нельзя, выведите одно число 0.

# Трэш полный!!! Нет смысла даже начинать!!!
