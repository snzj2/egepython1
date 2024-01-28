for A in range(1, 100):
    tr = True
    for x in range(100):
        for y in range(100):
            if (3 * x + 5 * y < A) or (x >= y) or (y > 8):
                pass
            else:
                tr = False
    if tr:
        print(A)