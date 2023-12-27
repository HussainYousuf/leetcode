class Solution:
    def getIntVal(self, c):
        if c == "I":
            return 1
        if c == "V":
            return 5
        if c == "X":
            return 10
        if c == "L":
            return 50
        if c == "C":
            return 100
        if c == "D":
            return 500
        if c == "M":
            return 1000

    def romanToInt(self, s: str) -> int:
        i = 0
        sum = 0
        while i < len(s):
            if (i + 1 < len(s)) and (
                (s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"))
                or (s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"))
                or (s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"))
            ):
                sum += self.getIntVal(s[i + 1]) - self.getIntVal(s[i])
                i += 2
            else:
                sum += self.getIntVal(s[i])
                i += 1

        return sum
