def tr(x):
    n = ""
    m = x
    while m != 0:
        n += str(m % 3)
        m = m // 3
    return n

def f(x):
    n = tr(x)
    if x % 3 != 0:
        l = tr((x % 3) * 5)
        n += l
    return int(n, 3)


for i in range(1, 100):
    if f(i) > 146:
        print(i)