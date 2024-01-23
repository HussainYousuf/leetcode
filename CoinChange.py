class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # optimal approach
        def dp(n, memo={}):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]

            q = 10**5  # amount max hence no number of coins (==1) is > than this
            for coin in coins:
                if n >= coin:
                    q = min(q, dp(n - coin) + 1)

            memo[n] = q
            return memo[n]

        res = dp(amount)
        if res == 10**5:
            return -1
        else:
            return res

        # amnt = amount

        # greedy approach

        # if amount == 0:
        #     return 0
        # coins.sort(reverse=True)
        # count = 0
        # for coin in coins:
        #     if amount >= coin:
        #         div = amount // coin
        #         count += div
        #         amount -= div * coin
        #         print(div, coin)

        # if amount != 0:

        # return count
