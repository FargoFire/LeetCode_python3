# coding:utf-8

"""
    Implement strStr().
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

    题目地址：https://leetcode.com/problems/implement-strstr/

    Date: 2019/06/23
    By: Fargo
    Difficulty: Easy
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not haystack and not needle:
            return 0

        n_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i: i+n_needle] == needle:
                return i
        return -1


haystack = ""
needle = "a"
out = Solution().strStr(haystack, needle)
print(out)



