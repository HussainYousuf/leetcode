# from leetcode
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def f(t1, t2, i, j, memo={}):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(t1):
                return 0
            if j == len(t2):
                return 0
            if t1[i] == t2[j]:
                memo[(i, j)] = 1 + f(t1, t2, i + 1, j + 1)
            if t1[i] != t2[j]:
                memo[(i, j)] = max(f(t1, t2, i + 1, j), f(t1, t2, i, j + 1))

            return memo[(i, j)]

        return f(text1, text2, 0, 0)


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
