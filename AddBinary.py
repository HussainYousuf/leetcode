def add_binary_integers(A, B):
    A = A[::-1]
    B = B[::-1]
    C = [0]
    i = 0
    while i < len(A):
        res = A[i] + B[i] + C[i]
        if res > 1:
            C.append(1)
        C[i] = res % 2
        i += 1
    return C[::-1]
