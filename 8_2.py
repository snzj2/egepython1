from itertools import product


cnt = 0
for i in product("ЛЕТО", repeat=4):
    if i[0] == "О" or i[0] == "Е":
        cnt += 1

print(cnt)
