"""
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random


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


k = 2
n1 = random.randint(0, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n = [n1, n2, n3]
st = ''
print(f"\nЗадана степень k = {k}.")


print(
    f"Сформирован многочлен со случайными коэффициентами --> {polynomial(n, k)}\n")

f = open('file_task_4.txt', 'w')
f.write(polynomial(n, k))
f.close()
