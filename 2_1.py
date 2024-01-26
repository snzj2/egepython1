for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x <= y) == (w or (not (z)))) == 0) and ((x <= y) and ((not (w)) == z)):
                    print(x, z, w, y)
print("##############")

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x <= y) == (w or (not (z)))) == 0):
                    print(x, z, w, y)

print("##############")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x <= y) and ((not (w)) == z)) == 0:
                    print(x, z, y, w)
