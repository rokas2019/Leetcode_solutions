# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(rf"{p}")
        return pattern.fullmatch(s)

# Runtime 314ms, Memory 13.9 MB
# Version without regex:

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

# Runtime 48ms, Memory 14.1MB
