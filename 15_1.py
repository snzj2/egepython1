for A in range(100):
    tr = True
    for m in range(100):
        for n in range(100):
            if (2 * m + 3* n > 43) or (m < A) or (n <= A):
                pass
            else:
                tr = False
    if tr:
        print(A)