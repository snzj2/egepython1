a = open("26-119.txt")

k = [int(i) for i in a.readline().split()]
n = []
for i in a.readlines():
    m = i.split()

    n.append([int(m[0]), int(m[1]), m[2]])

n.sort()
print(n)
M = [] * k[2]
L = [] * k[1]

for i in n:
    if i[2] == "A":
        b = 1
        for j in range(k[1]):
            if