# coding:utf-8

"""
    Given a 32-bit signed integer, reverse digits of an integer.
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed
    integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function
    returns 0 when the reversed integer overflows.

    题目地址:https://leetcode.com/problems/reverse-integer/

    Date: 2019/06/03
    By: Fargo
    Difficulty: Easy
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            m = str(abs(x))[::-1]
            m = -1 * int(m)
        else:
            m = int(str(x)[::-1])

        max = math.pow(2, 31) - 1
        min = -1 * math.pow(2, 31)
        if m > max:
            return 0
        elif m < min:
            return 0
        else:
            return m