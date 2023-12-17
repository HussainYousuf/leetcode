# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    distance = numRows + (numRows - 2)
    res = ""
    for i in range(numRows):
        otherDistance = None
        if i != 0 and i != numRows - 1:
            otherDistance = distance - (i * 2)

        j = i
        while j < len(s):
            res += s[j]
            if otherDistance is not None and j + otherDistance < len(s):
                res += s[j + otherDistance]
            j += distance

    return res


print(convert("A", 1))
