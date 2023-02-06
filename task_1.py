""" 
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    

      10^{-1} ≤ d ≤ 10^{-10}

          0.1 ≤ d ≤  0.00000000001
          число Pi = 3.1415926535

          ряд Лейбница
          π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
          3.14159264958921 500_000_000 итераций, ряд Лейбница

          ряд Нилаканта
          π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
          3.141592653589789 100_000 итераций, ряд Нилаканта
"""
import random


iterations = 1_000_000
n = random.randint(1, 10)
d = "0."
for i in range(1, n):
    d = d + '0'
d = d + '1'


def pi_Nilakanta(it):  # ряд Нилаканта
    pi = 0
    s = 1
    pi = 3
    for i in range(2, it, 2):
        if s < 0:
            pi -= 4/(i*(i+1)*(i+2))
            s *= -1
        elif s > 0:
            pi += 4/(i*(i+1)*(i+2))
            s *= -1
    return pi


def pi_Leibniza(it):  # ряд Лейбница
    pi = 0
    s = 1
    pi = 4/1 - 4/3
    for i in range(5, it, 2):
        if s < 0:
            pi -= 4/i
            s *= -1
        elif s > 0:
            pi += 4/i
            s *= -1
    return pi


print("\nВычисления числа ПИ (ряд Нилаканта) с заданной точность d = ", end='')
print(f"{d} --> {round(pi_Nilakanta(iterations), n)}\n")
print("Вычисления числа ПИ (ряд Лейбница)  с заданной точность d = ", end='')
print(f"{d} --> {round(pi_Leibniza(iterations), n)}\n")