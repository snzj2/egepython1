a = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1

k = []

while a != 0:
    k.append(a % 16)
    a //= 16

print(k.count(0))