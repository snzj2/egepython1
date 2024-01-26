a = open("17_1.txt")
m = a.readlines()

n = [int(i.strip()) for i in m]
mx = 0
cnt = 0
for i in range(len(n)):
    for j in range(i, len(n)):
        if (((n[i] + n[j])) % 80 == 0) and (n[i] % 50 == 0 or n[j] % 50 == 0):
            mx = max((n[i] + n[j]), mx)
            cnt += 1

print(mx, cnt)
