# coding:utf-8

"""
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example 1:
    Input: 121
    Output: true

    题目地址： https://leetcode.com/problems/palindrome-number/

    Date: 2019/06/07
    By: Fargo
    Difficulty: Easy
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 : return False

        if x >= 0:
            x = str(x)
            m = 0
            for i in range(len(x)):
                if x[i] != x[len(x)-i-1]:
                    m += 1
            if m == 0 : return True
            else : return False


print(Solution().isPalindrome(1001))
