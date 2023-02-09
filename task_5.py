"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""


def decoPolyn(st):
    """ 
    Разложение многочлена
    """
    n1 = n2 = n3 = ''
    for i in range(0, len(st)):
        if st[i] == '^':
            for j in range(0, i-1):
                n1 += st[j]
        elif st[i] == 'x':
            for t in range(0, i):
                if st[t] == '+':
                    for r in range(t + 1, i):
                        n2 += st[r]
        elif st[i] == '=':
            for m in range(t, len(st)):
                if st[m] == '+':
                    for q in range(m + 1, i):
                        n3 += st[q]
    stpoly = []
    stpoly = [int(n1), int(n2), int(n3)]
    return stpoly


def polynomial(n, k):
    """
    Создание многочлена
    """
    st = ''
    for i in range(0, 3):
        if i == 0 and n[i] > 0:
            if n[i] == 1:
                st += 'x'+'^' + str(k)
            else:
                st += str(n[i]) + 'x'+'^' + str(k)

        if i == 1 and n[i] > 0:
            if n[i] == 1 and n[i-1] > 0:
                st += '+'+'x'
            elif n[i] == 1 and n[i-1] == 0:
                st += 'x'
            elif n[i-1] != 0:
                st += '+' + str(n[i]) + 'x'
            else:
                st += str(n[i]) + 'x'
        elif i == 2 and n[i] > 0:
            st += '+' + str(n[i])

    st += ''+'=' + '0'
    return st


st1 = st2 = st3 = ''

f1 = open('file_task_5_1.txt', 'r')
st1 = f1.readline()
f1.close()

f2 = open('file_task_5_2.txt', 'r')
st2 = f2.readline()
f2.close()

print(f"\nИнформация с файла 1, многочлен --> {st1}")
print(f"Информация с файла 2, многочлен --> {st2}")
print(f"Сложение многочленов {st1} и {st2}:")

st1list = decoPolyn(st1)[:]
st2list = decoPolyn(st2)[:]
st3list = []

for i in range(0, len(st1list)):
    st3list.append(st1list[i] + st2list[i])

st3 = polynomial(st3list, k=2)[:]

print(f"({st1[:-2]})", end=' + ')
print(f"({st2[:-2]})", end=' =')
print(f" {st3[:-2]}\n")

f3 = open('file_task_5_3.txt', 'w')
f3.write(st3)
f3.close()
