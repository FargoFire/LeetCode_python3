# coding: utf-8


"""
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    Example 1:  Input: "babad"    Output: "bab"
    Note: "aba" is also a valid answer.

    题目链接： https://leetcode.com/problems/longest-palindromic-substring/

    Date: 2019/06/04
    By: Fargo
    Difficulty: Medium
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = ''
        n = len(s)

        # 第一种 "babad"
        for i in range(n):
            j = k = i
            while j >= 0 and k < n and s[j] ==s[k]:
                j -=1
                k +=1
            palindrome1 = s[j + 1:k]

            if len(palindrome1) > len(lp):
                lp =palindrome1

        # 第二种 "babbac"
        for i in range(n):
            j = i
            k = i+1
            while j >= 0 and k < n and s[j] == s[k]:
                j -= 1
                k += 1
            palindrome2 = s[j+1:k]

            if len(palindrome2) > len(lp):
                lp =palindrome2

        return lp


print(Solution().longestPalindrome('abbcacbdb'))

