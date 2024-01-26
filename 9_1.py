a = open("9_1.txt")

b = a.readlines()
cnt = 0
for i in b:
    k = [int(j.strip()) for j in i.split()]

    k = sorted(k)

    if (k[0] + k[4]) ** 2 > k[1] ** 2 + k[2] ** 2 + k[3] ** 2:
        cnt += 1

print(cnt)