def f(a, b):
    if b <= 1:
        return a
    else:
        return a * f(a, b - 1)


a = 3
b = 5
print(f(a, b))
