print(4 * 6 ** 20)

def f(x):
    if x < 9:
        return x
    else:
        return f(x % 9) + f(x // 9)

for i in range(4 * 6 ** 20, 5 * 6 ** 20):
    if f(i) == 121:
        print(i)