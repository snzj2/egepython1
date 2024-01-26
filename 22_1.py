with open("22_1.txt") as file:
    processes = {"0": range(0, 1)}

    for line in file.readlines():
        num, time, sub = line.split()
        start_time = max([max(processes[i]) for i in sub.split(";")])
        processes[num] = range(start_time, start_time + int(time) + 1)

counter = 0
for time in processes.values():
    if 150 in time:
        counter += 1

print(counter)