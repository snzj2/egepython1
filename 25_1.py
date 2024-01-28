for i in range(10):
    cnt = 0
    while int(f"1{i}7246{cnt}1") < 10 ** 10:
        if int(f"1{i}7246{cnt}1") % 4173 == 0:
            print((f"1{i}7246{cnt}1"))
        cnt += 1
    if int(f"1{i}72461") % 4173 == 0:
        print((f"1{i}72461"))