class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if res < -(2**31) or res > 2**31 - 1:
            return 0
        if x < 0:
            return -res
        else:
            return res
