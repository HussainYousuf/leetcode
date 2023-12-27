def lcs(X, Y):
    if not X or not Y:
        return ""
    x = X[0]
    y = Y[0]
    if x == y:
        return x + lcs(X[1:], Y[1:])
    else:
        s1 = lcs(X[1:], Y)
        s2 = lcs(X, Y[1:])
        if len(s1) > len(s2):
            return s1
        else:
            return s2


def lcsMem(X, Y, holder={}):
    if not X or not Y:
        return ""

    if (X, Y) not in holder:
        x = X[0]
        y = Y[0]
        if x == y:
            holder[X, Y] = x + lcs(X[1:], Y[1:])
        else:
            s1 = holder[X[1:], Y] = lcs(X[1:], Y)
            s2 = holder[X, Y[1:]] = (
                holder[X, Y[1:]] if (X, Y[1:]) in holder else lcs(X, Y[1:])
            )
            if len(s1) > len(s2):
                return s1
            else:
                return s2
    return holder[X, Y]


print(lcsMem("ACCGG", "GTCG"))
print(lcsMem("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA"))
