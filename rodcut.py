import math

# Rn = max(Pi+Rn-i)


def rodCut(P, n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(n):
        if i not in P:
            P.append(0)
        q = max(q, P[i] + rodCut(P, n - 1 - i))
    return q


def rodCutMem(P, n, holder={}):
    holder[0] = 0
    if n not in holder:
        q = -math.inf
        for i in range(n):
            if i not in P:
                P.append(0)
            q = max(q, P[i] + rodCutMem(P, n - 1 - i))
        holder[n] = q

    return holder[n]


print([rodCutMem([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], i) for i in range(1, 40)])
