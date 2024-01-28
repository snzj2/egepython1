from itertools import product


cnt = 0

for i in product("ABCX", repeat=5):
    if i[0] == "X" and ("".join(i)).count("X") == 1:
        cnt += 1

print(cnt)
print(1 * 3 * 3 * 3 * 3)