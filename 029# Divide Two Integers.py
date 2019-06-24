# coding:utf-8

"""
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.

    Example 1:  Input: dividend = 10, divisor = 3   Output: 3

    Note:
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division
     result overflows.

    题目地址：https://leetcode.com/problems/divide-two-integers/

    Date: 2019/06/24
    By: Fargo
    Difficulty: Medium
"""
import time

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_num, min_num = 2147483647, -2147483648
        idend, isor = abs(dividend), abs(divisor)
        res = 0

        # while idend >= isor:
        #     idend -= isor
        #     res += 1

        # 位运算
        while idend >= isor:
            temp, i = isor, 1
            while idend >= temp:
                idend -= temp
                res += i
                i <<= 1
                temp <<= 1

        if (dividend < 0) != (divisor < 0):
            res = -res
        res = max(min(res, max_num), min_num)
        return res

        # positive = (dividend < 0) is (divisor < 0)
        # dividend, divisor = abs(dividend), abs(divisor)
        # res = 0
        # while dividend >= divisor:
        #     temp, i = divisor, 1
        #     while dividend >= temp:
        #         dividend -= temp
        #         res += i
        #         i <<= 1
        #         temp <<= 1
        # if not positive:
        #     res = -res
        # return min(max(-2147483648, res), 2147483647)


start = time.clock()
dividend = -2147483648
divisor = 1
out = Solution().divide(dividend, divisor)
print(out, time.clock()-start)



