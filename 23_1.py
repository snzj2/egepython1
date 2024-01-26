def f(x, tr):
    if x == 9:
        tr = True
    if x == 15:
        tr = False
    if x == 20 and tr:
        return 1
    if x > 20:
        return 0
    if x >= 16 and (tr == False):
        return 0
    return f(x + 1, tr) + f(x + 2, tr)

print(f(3, False))
