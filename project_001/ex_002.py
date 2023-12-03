def func_prog(a, d, n):
    prog = []
    prog.append(a)
    i = 2
    while i <= n:
        prog.append(a + d * (i - 1))
        i += 1
    return prog


start_n = int(input('Введите первый элемент арифметической прогрессии: '))
delta = int(input('Введите шаг прогрессии: '))
sum_n = int(input('Введите количество элементов прогрессии: '))

print(func_prog(start_n, delta, sum_n))
