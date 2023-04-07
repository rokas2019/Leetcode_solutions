# Given a string s, find the length of the longest
# substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        i = j = 0
        longest_substring_len = 0
        chars = set()

        while i < n and j < n:
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                longest_substring_len = max(longest_substring_len, j - i)
            else:
                chars.remove(s[i])
                i += 1

        return longest_substring_len


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = 0
        m = 0
        d = {}
        for i, v in enumerate(s):
            if v in d and st <= d[v]:
                st = d[v] + 1
            else:
                m = max(m, i - st + 1)
            d[v] = i

        return m

# In this code, i and j are the left and right indices of the sliding window, respectively. We use a set chars to
# keep track of the characters in the current window. We move the window to the right by incrementing j until we
# encounter a repeating character. Whenever we encounter a repeating character, we remove the leftmost character(s)
# from the window by incrementing i and removing s[i] from the set chars. We update longest_substring_len whenever we
# add a new character to the window.
#
# For the input "abcabcbb", this function will return 3, which is the length of the longest substring without
# repeating characters ("abc").
