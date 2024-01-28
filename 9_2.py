a = open("9_2.txt")

k = a.readlines()
cnt = 0
for i in k:
    n = [int(j) for j in i.split()]

    k = sorted(n)
    if len(set(k)) == 5:
        cn = cn1 = 0
        for j in set(n):
            if n.count(j) == 2:
                cn += j * 2
            else:
                cn1 += j
        if cn:
            if (cn / 4) < ((sum(k) - cn) / 3):
                cnt += 1

print(cnt)