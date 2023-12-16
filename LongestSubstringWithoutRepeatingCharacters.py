# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        acc = ""
        maxLen = 0
        for c in s:
            if c in acc:
                acc = acc[acc.index(c) + 1 :]
            acc += c
            if len(acc) > maxLen:
                maxLen = len(acc)
        return maxLen
