class Solution:
    def climbStairs(self, n: int) -> int:
        def f(n, memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            res = f(n - 1, memo)
            if n >= 2:
                res += f(n - 2, memo)
            memo[n] = res
            return res

        return f(n, {})
