def f(n, x):
    if x == 4 and n >= 30:
        return 1
    if x == 4 and n < 30:
        return 0
    if x < 4 and n >= 30:
        return 0
    if x % 2 == 0:
        return f(n + 1, x + 1) and f(n * 3, x + 1)
    if x % 2 != 0:
        return f(n + 1, x + 1) or f(n * 3, x + 1)


for i in range(1, 29):
    if f(i, 1):
        print(i)