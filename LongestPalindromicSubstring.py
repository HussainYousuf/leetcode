# Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = ""
        i = 0
        while i < len(s):
            l = i - 1
            r = i + 1
            palindrome = ""

            while r < len(s) and s[i] == s[r]:
                r += 1

            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            palindrome = s[l + 1 : r]

            if len(palindrome) > len(maxPalindrome):
                maxPalindrome = palindrome

            i += 1

        return maxPalindrome
