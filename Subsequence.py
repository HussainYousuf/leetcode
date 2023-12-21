from AllBinary import AllBinary


def genSubsequence(s):
    res = []
    for arr in AllBinary().genBin(len(s)):
        newStr = ""
        for i in range(len(s)):
            if arr[i]:
                newStr += s[i]
        res.append(newStr)
    return res


print(genSubsequence("a"))
print(genSubsequence("ab"))
print(genSubsequence("abc"))
