# coding:utf-8

"""
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
    represented as a string.

    Example 1:  Input: num1 = "2", num2 = "3"  Output: "6"

    Note:
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

    题目地址：https://leetcode.com/problems/multiply-strings/

    Date: 2019/07/06
    By: Fargo
    Difficulty: Medium
"""
import time

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1_unit, n2_unit = 1, 1
        result = 0

        for n1 in reversed(num1):
            n1 = int(n1) * n1_unit
            for n2 in reversed(num2):
                n2 = int(n2) * n2_unit
                result += n1 * n2
                n2_unit = n2_unit * 10
            n1_unit = n1_unit * 10
            n2_unit = 1
        return str(result)


start = time.clock()
num1 = '123'
num2 = '45'
out = Solution().multiply(num1, num2)
print(out, time.clock()-start)



