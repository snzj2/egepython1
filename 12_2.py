

def f(x):
    n = ""
    while "21" in x:
        x = x.replace("21", "5", 1)

    return sum([int(i) for i in x])

for i in range(1, 1000):
    if f("1" * 10 + "2" * i) == 34:
        print(i)
