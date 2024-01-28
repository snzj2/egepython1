def f(x):

    n = int(x[0]) * int(x[1])
    n1 = int(x[1]) * int(x[2])
    k = sorted([n1, n])

    return int(str(k[0]) + str(k[1]))

for i in range(100, 1000):
    if f(str(i)) == 621:
        print(i)