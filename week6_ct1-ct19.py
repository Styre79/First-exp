# 1 Слияние списков
# Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините их в один упорядоченный список С
# (то есть он должен содержать len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B),
# возвращающей новый список. Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается. Использовать функцию sorted и метод sort запрещается.
# Программа получает на вход два неубывающих списка, каждый в отдельной строке.
def merge(a, b):
    c = []
    inda, indb = 0, 0
    while inda < len(a) and indb < len(b):
        if a[inda] <= b[indb]:
            c.append(a[inda])
            inda += 1
        else:
            c.append(b[indb])
            indb += 1
    if inda == len(a):
        c.extend(b[indb:])
    else:
        c.extend(a[inda:])
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))

# 2* Пересечение множеств
# Даны два списка, упорядоченных по возрастанию (каждый список состоит из различных элементов).
# Найдите пересечение множеств элементов этих списков, то есть те числа, которые являются элементами обоих списков.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Решение оформите в виде функции Intersection(A, B).
# Функция должна возвращать список пересечения данных списков в порядке возрастания элементов.
# Модифицировать исходные списки запрещается.
def intersection(a, b):
    c = []
    inda, indb = 0, 0
    while inda < len(a) and indb < len(b):
        if a[inda] < b[indb]:
            inda += 1
        elif a[inda] == b[indb]:
            c.append(a[inda])
            inda += 1
            indb += 1
        else:
            indb += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*intersection(a, b))

# 3 Сортировка
# Отсортируйте данный массив, используя встроенную сортировку.
# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 10⁵.
# Далее идет N целых чисел, не превосходящих по абсолютной величине 10⁹.
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(*a)

# 4* Обувной магазин
# В обувном магазине продается обувь разного размера. Известно, что одну пару обуви можно надеть на другую,
# если она хотя бы на три размера больше. В магазин пришел покупатель.Требуется определить,
# какое наибольшее количество пар обуви сможет предложить ему продавец так, чтобы он смог надеть их все одновременно.
# Сначала вводится размер ноги покупателя (обувь меньшего размера он надеть не сможет), в следующей строке — размеры
# каждой пары обуви в магазине через пробел. Размер — натуральное число, не превосходящее 100.
# Выведите единственное число — максимальное количество пар обуви, которое сможет надеть покупатель.
size = int(input())
a = list(map(int, input().split()))
count = 0
a.sort()
for i in a:
    if i >= size:
        count += 1
        size = i+3
print(count)

# 5 Создание архива
# Системный администратор вспомнил, что давно не делал архива пользовательских файлов. Однако, объем диска,
# куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о пользователях и свободному объему на архивном диске
# определит максимальное число пользователей, чьи данные можно поместить в архив.
# Программа получает на вход в одной строке число S – размер свободного места на диске
# (натуральное, не превышает 10000), и число N – количество пользователей (натуральное, не превышает 100),
# после этого идет N чисел - объем данных каждого пользователя (натуральное, не превышает 1000),
# записанных каждое в отдельной строке.
data = []
size, users = map(int, (input().split()))
for i in range(users):
    data.append(int(input()))
data.sort()
users_in_arch = 0
while size >= 0 and users_in_arch < users:
    size -= data[users_in_arch]
    users_in_arch += 1
print(users_in_arch) if size >= 0 else print(users_in_arch - 1)

# 6 Гражданская оборона
# Штаб гражданской обороны Тридесятой области решил обновить план спасения на случай ядерной атаки.
# Известно, что все n селений Тридесятой области находятся вдоль одной прямой дороги.
# Вдоль дороги также расположены m бомбоубежищ, в которых жители селений могут укрыться на случай ядерной атаки.
# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.

# В первой строке вводится число n - количество селений (1 <= n <= 100000).
# Вторая строка содержит n различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до i-го селения.
# В третьей строке входных данных задается число m - количество бомбоубежищ (1 <= m <= 100000).
# Четвертая строка содержит m различных целых чисел, i-е из этих чисел задает расстояние от начала дороги
# до i-го бомбоубежища. Все расстояния положительны и не превышают 10⁹.
# Селение и убежище могут располагаться в одной точке.

# Выведите  n чисел - для каждого селения выведите номер ближайшего к нему бомбоубежища.
# Бомбоубежища пронумерованы от 1 до m в том порядке, в котором они заданы во входных данных.

# Создайте список кортежей из пар (позиция селения, его номер в исходном списке),
# а также аналогичный список для бомбоубежищ. Отсортируйте эти списки.
# Перебирайте селения в порядке возрастания.
# Для селения ближайшими могут быть два соседних бомбоубежища, среди них надо выбрать ближайшее.
# При переходе к следующему селению не обязательно искать ближайшее бомбоубежище с самого начала.
# Его можно искать начиная с позиции, найденной для предыдущего города.
# Аналогично, не нужно искать подходящее бомбоубежище до конца списка бомбоубежищ: достаточно найти самое близкое.
# Если Вы неэффективно реализуете эту часть, то решение тесты не пройдет.
# Для хранения ответа используйте список, где индекс будет номером селения,
# а по этому индексу будет запоминаться номер бомбоубежища.
cities, shelters, = [], []
qty_cities = int(input())
tmp = list(map(int, input().split()))
for i in range(qty_cities):
    cities.append((tmp[i], i))
qty_shelters = int(input())
tmp = list(map(int, input().split()))
for i in range(qty_shelters):
    shelters.append((tmp[i], i+1))
cities.sort()
shelters.sort()
result = [0]*qty_cities
ind = 0
for city in cities:
    while ind < len(shelters)-1 \
            and abs(city[0]-shelters[ind][0]) \
            > abs(city[0]-shelters[ind+1][0]):
        ind += 1
    if ind == len(shelters) - 1:
        result[city[1]] = shelters[ind][1]
    elif abs(city[0]-shelters[ind][0]) \
            <= abs(city[0]-shelters[ind+1][0]):
        result[city[1]] = shelters[ind][1]
print(*result)

# 7* Средний балл по классам
# В олимпиаде по информатике принимало участие несколько человек.
# Определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:
# фамилия имя класс балл.
# Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из трех чисел 9, 10, 11.
# Балл - целое число от 0 до 100.
# В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.
# Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу.
# Входной файл в кодировке utf-8 (используйте open('input.txt', 'r', encoding='utf-8')).
qty9, qty10, qty11 = 0, 0, 0
sum9, sum10, sum11 = 0, 0, 0
inf = open('input.txt', 'r', encoding='utf-8')
for line in inf:
    line = line.strip().split()
    group, score = int(line[2]), int(line[3])
    if group == 9:
        qty9 += 1
        sum9 += score
    if group == 10:
        qty10 += 1
        sum10 += score
    if group == 11:
        qty11 += 1
        sum11 += score
inf.close()
print(sum9 / qty9, sum10 / qty10, sum11 / qty11)
# второй вариант через класс, как структуру данных
class Students:
    surname = ''
    name = ''
    group = 0
    score = 0


studlist =[]
inf = open('input6week.txt', 'r', encoding='utf-8')
for line in inf:
    line = line.strip().split()
    student = Students()
    student.group = int(line[2])
    student.score = int(line[3])
    studlist.append(student)
inf.close()
c9, c10, c11 = 0, 0, 0
ascore9, ascore10, ascore11 = 0, 0, 0
for student in studlist:
    if student.group == 9:
        c9 += 1
        ascore9 += student.score
    elif student.group == 10:
        c10 +=1
        ascore10 += student.score
    elif student.group == 11:
        c11 += 1
        ascore11 += student.score
print(c9, c10, c11)
print(ascore9, ascore10, ascore11)
print(ascore9 / c9, ascore10 / c10, ascore11/ c11)

# 8 Отсортировать список участников по алфавиту
# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').
# Входные данные: Строки вида "Фамилия Имя НомерШколы Балл".
# Выходные данные: Строки вида "Фамилия Имя Балл", отсортированные по фамилии.
studentslist = []
inf = open('input.txt', 'r', encoding='utf-8')
for line in inf:
    student = line.split()
    if student:
        student.pop(2)
        studentslist.append(' '.join(student))
inf.close()
studentslist.sort()
ouf = open('output.txt', 'w', encoding='utf-8')
ouf.write('\n'.join(studentslist))
ouf.write('\n')
ouf.close()

# 9 Сортировка подсчетом
# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
# Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
# Использовать встроенные функции сортировки нельзя.
def countsort(a, qty_dif_val=101):
    qvallist = [0] * qty_dif_val
    for i in a:
        qvallist[i] += 1
    lensortlist = len(a)
    a.clear()
    for i in range(len(qvallist)):
        if qvallist[i]:
            a.extend([i] * qvallist[i])
        if len(a) == lensortlist:
            break
    return a


a = list(map(int, input().split()))
print(*countsort(a))

# 10* Клавиатура
# На региональном этапе Всероссийской олимпиады школьников по информатике в 2009 году предлагалась следующая задача.
# Всем известно, что со временем клавиатура изнашивается, и клавиши на ней начинают залипать. Конечно, некоторое время
# такую клавиатуру еще можно использовать, но для нажатий клавиш приходиться использовать большую силу.
# При изготовлении клавиатуры изначально для каждой клавиши задается количество нажатий, которое она должна выдерживать.
# Если знать эти величины для используемой клавиатуры, то для определенной последовательности нажатых клавиш
# можно определить, какие клавиши в процессе их использования сломаются, а какие — нет.
# Требуется написать программу, определяющую,
# какие клавиши сломаются в процессе заданного варианта эксплуатации клавиатуры.
# Первая строка входных данных содержит целое число n (1≤n≤1000) — количество клавиш на клавиатуре.
# Вторая строка содержит n целых чисел —с₁, с₂, … , сn, где сᵢ (1≤cᵢ≤100000) — количество нажатий,
# выдерживаемых i-ой клавишей. Третья строка содержит целое число k (1≤k≤100000) — общее количество нажатий клавиш,
# и последняя строка содержит k целых чисел pj (1≤pj≤n) — последовательность нажатых клавиш.
# Программа должна вывести n строк, содержащих информацию об исправности клавиш. Если i-я клавиша сломалась,
# то i-ая строка должна содержать слово YES, если же клавиша работоспособна — слово NO.
n_key = int(input())
qty_press = list(map(int, input().split()))
k_press = int(input())
num_press_key = list(map(int, input().split()))
for i in num_press_key:
    qty_press[i-1] -= 1
for i in qty_press:
    if i >= 0:
        print('NO')
    else:
        print('YES')

# 11* Максимальный балл по классам
# В олимпиаде по информатике принимало участие несколько человек. Победителем олимпиады становится человек,
# набравший больше всех баллов. Победители определяются независимо по каждому классу. Определите количество баллов,
# которое набрал победитель в каждом классе. Гарантируется, что в каждом классе был хотя бы один участник.
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:фамилия имя класс балл.
# Фамилия и имя — текстовые строки, не содержащие пробелов.
# Класс - одно из трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
# В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.
# Выведите три числа: баллы победителя олимпиады по 9 классу, по 10 классу, по 11 классу.
# Входной файл в кодировке utf-8 (В Python используйте open('input.txt', 'r', encoding='utf-8')).
max9, max10, max11 = 0, 0, 0
inf = open('input.txt', 'r', encoding='utf-8')
for student in inf:
    student = student.strip().split()
    if student:
        if student[2] == '9' and int(student[3]) > max9:
            max9 = int(student[3])
        if student[2] == '10' and int(student[3]) > max10:
            max10 = int(student[3])
        if student[2] == '11' and int(student[3]) > max11:
            max11 = int(student[3])
inf.close()
print(max9, max10, max11)

# 12 Результаты олимпиады
# В олимпиаде участвовало N человек. Каждый получил определенное количество баллов, при этом оказалось, что у всех
# участников разное число баллов. Упорядочите список участников олимпиады в порядке убывания набранных баллов.
# Программа получает на вход число участников олимпиады N. Далее идет N строк,
# в каждой строке записана фамилия участника, затем, через пробел, набранное им количество баллов.
# Выведите список участников (только фамилии) в порядке убывания набранных баллов.
students = []
n = int(input())
for i in range(n):
    students.append(tuple(input().split()))
students.sort(key=lambda x: int(x[1]), reverse=True)
for student in students:
    print(student[0])

# 13* Количество победителей по классам
# В условиях предыдущей задачи определите количество школьников, ставших победителями в каждом классе.
# Победителями объявляются все, кто набрал наибольшее число баллов по данному классу.
# Гарантируется, что в каждом классе был хотя бы один участник.
# Выведите три числа: количество победителей олимпиады по 9 классу, по 10 классу, по 11 классу.
max9, max10, max11 = 0, 0, 0
win9, win10, win11 = 0, 0, 0
inf = open('input.txt', 'r', encoding='utf-8')
for student in inf:
    student = student.strip().split()
    if student:
        if student[2] == '9':
            if int(student[3]) == max9:
                win9 += 1
            elif int(student[3]) > max9:
                max9 = int(student[3])
                win9 = 1
        if student[2] == '10':
            if int(student[3]) == max10:
                win10 += 1
            elif int(student[3]) > max10:
                max10 = int(student[3])
                win10 = 1
        if student[2] == '11':
            if int(student[3]) == max11:
                win11 += 1
            elif int(student[3]) > max11:
                max11 = int(student[3])
                win11 = 1
inf.close()
print(win9, win10, win11)

# 14 Проходной балл
# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ,
# каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты, набравшие менее 40 баллов
# (неудовлетворительную оценку) по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе
# по сумме баллов за три экзамена. В конкурсе участвует N человек, при этом количество мест равно K.
# Определите проходной балл, то есть такое количество баллов, что количество участников,
# набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов, набравших наибольшее
# количество баллов среди непринятых абитуриентов, общее число принятых абитуриентов станет больше K.
# Программа получает на вход количество мест K. Далее идут строки с информацией об абитуриентах,
# каждая из которых состоит из имени (текстовая строка содержащая произвольное число пробелов) и трех чисел от 0 до 100,
# разделенных пробелами. Используйте для ввода файл input.txt с указанием кодировки utf8
# (для создания такого файла на своем компьютере в программе Notepad++ следует использовать кодировку UTF-8 без BOM).
# Программа должна вывести проходной балл в конкурсе. Выведенное значение должно быть минимальным баллом,
# который набрал абитуриент, прошедший по конкурсу. Также возможны две ситуации, когда проходной балл не определен.
# Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.
# Если количество имеющих равный максимальный балл абитуриентов больше чем K, программа должна вывести число 1.
# Используйте для вывода файл output.txt с указанием кодировки utf8.
all_qualify = []
winners = []
inf = open('input.txt', 'r', encoding='utf-8')
n = int(inf.readline().strip())
for student in inf:
    student = student.strip().split()
    if student:
        sc1, sc2, sc3 = int(student[-3]), int(student[-2]), int(student[-1])
        if sc1 > 39 and sc2 > 39 and sc3 > 39:
            all_qualify.append(sc1 + sc2 + sc3)
inf.close()
all_qualify.sort()
for i in range(n):
    if all_qualify:
        winners.append(all_qualify.pop())
if all_qualify:
    if winners[0] == all_qualify[-1]:
        res = 1
    else:
        winners.reverse()
        for i in range(len(winners)):
            if winners[i] > all_qualify[-1]:
                res = winners[i]
                break
else:
    res = 0
ouf = open('output.txt', 'w')
print(res, file=ouf)
ouf.close()

# 15* Школы с наибольшим числом участников олимпиады
# В олимпиаде по информатике принимало участие N человек. Определите школы, из которых в олимпиаде принимало участие
# больше всего участников. В этой задаче необходимо считывать данные построчно,
# не сохраняя в памяти данные обо всех участниках, а только подсчитывая число участников для каждой школы.
# Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
# фамилия имя школа балл
# Фамилия и имя— текстовые строки, не содержащие пробелов.Школа — целое число от 1 до 99.Балл — целое число от 0 до 100.
# Выведите номера этих школ в порядке возрастания.
schools = [0]*100
inf = open('input.txt', 'r', encoding='utf-8')
for student in inf:
    student = student.strip().split()
    if student:
        schools[int(student[-2])] += 1
inf.close()
ind = 0
count = schools.count(max(schools))
maxstud = max(schools)
for i in range(count):
    print(schools.index(maxstud, ind), end=' ')
    ind = schools.index(maxstud, ind) + 1

# 16* Максимальный балл не-победителя
# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники,
# которые набрали наибольший балл среди всех участников в данном классе.
# Для каждого класса определите максимальный балл, который набрал школьник, не ставший победителем в данном классе.
# Выведите три целых числа.
s9, s10, s11 = [], [], []
inf = open('input.txt', 'r', encoding='utf-8')
for student in inf:
    student = student.strip().split()
    if student:
        if student[-2] == '9' and int(student[-1]) not in s9:
            s9.append(int(student[-1]))
        if student[-2] == '10' and int(student[-1]) not in s10:
            s10.append(int(student[-1]))
        if student[-2] == '11' and int(student[-1]) not in s11:
            s11.append(int(student[-1]))
inf.close()
s9.sort()
s10.sort()
s11.sort()
print(s9[-2], s10[-2], s11[-2])

# 17* Такси
# После затянувшегося совещания директор фирмы решил заказать такси, чтобы развезти сотрудников по домам. Он заказал
# N машин — ровно столько, сколько у него сотрудников. Однако когда они подъехали, оказалось, что у каждого водителя
# такси свой тариф за 1 километр. Директор знает, какому сотруднику сколько километров от работы до дома
# (к сожалению, все сотрудники живут в разных направлениях, поэтому нельзя отправить двух сотрудников на одной машине).
# Теперь директор хочет определить, сколько придется заплатить за перевозку всех сотрудников.
# Естественно, директор хочет заплатить как можно меньшую сумму.
# В первой строке записаны N чисел через пробел, задающих расстояния в километрах от работы до домов
# сотрудников компании. Во второй строке записаны N чисел — тарифы за проезд одного километра в такси.
# Выведите одно целое число — наименьшую сумму, которую придется заплатить за доставку всех сотрудников.
distances = list(map(int, input().split()))
taxes = list(map(int, input().split()))
distances.sort()
taxes.sort(reverse=True)
total = sum(list(map(lambda x, y: x * y, distances, taxes)))
print(total)

# 18* Семипроцентный барьер
# В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам.
# Каждый избиратель указывает одну партию, за которую он отдает свой голос. В Государственную Думу попадают партии,
# которые набрали не менее 7% от числа голосов избирателей.
# Дан список партий и список голосов избирателей. Выведите список партий, которые попадут в Государственную Думу.
# В первой строке входного файла написано слово PARTIES:. Далее идет список партий, участвующих в выборах.
# Затем идет строка, содержащая слово VOTES:. За ним идут названия партий, за которые проголосовали избиратели,
# по одному названию в строке. Названия могут быть только строками из первого списка.
# Программа должна вывести названия партий, получивших не менее 7% от числа голосов в том порядке,
# в котором они следуют в первом списке.
inf = open('input.txt', 'r', encoding='utf-8')
for par_and_vot in inf:
    par_and_vot = par_and_vot.strip()
    if par_and_vot:
        if par_and_vot == 'PARTIES:':
            parties = []
            porv = 1
        if par_and_vot == 'VOTES:':
            votes = []
            porv = 0
        if porv:
            parties.append(par_and_vot)
        else:
            votes.append(par_and_vot)
qty_votes = (len(votes) - 1)
total_votes = [0] * len(parties)
for i in range(1, len(votes)):
    total_votes[parties.index(votes[i])] += 1
for i in range(1, len(total_votes)):
    if total_votes[i] / qty_votes >= 0.07:
        print(parties[i])

# 19* Упорядочить список партий по числу голосов
# Формат входных данных аналогичен предыдущей задаче. Выведите список всех партий, участвовавших в выборах,
# отсортировав его в порядке убывания количества голосов избирателей,
# а при равном количестве голосов - в лексикографическом порядке.
inf = open('input.txt', 'r', encoding='utf-8')
for par_and_vot in inf:
    par_and_vot = par_and_vot.strip()
    if par_and_vot:
        if par_and_vot == 'PARTIES:':
            parties = []
            porv = 1
        if par_and_vot == 'VOTES:':
            votes = []
            porv = 0
        if porv:
            parties.append(par_and_vot)
        else:
            votes.append(par_and_vot)
total_votes = [0] * len(parties)
for i in range(1, len(votes)):
    total_votes[parties.index(votes[i])] += 1
tup_list = [(total_votes[i], parties[i]) for i in range(1, len(parties))]
tup_list.sort(key=lambda x: (-x[0], x[1]))
for party in tup_list:
    print(party[1])
