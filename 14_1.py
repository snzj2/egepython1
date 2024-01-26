a = 16 ** 8 * 4 ** 20 - 4 ** 5 - 64
n = ""
while a != 0:
    n += str(a % 4)
    a = a // 4

print(n.count("3"))