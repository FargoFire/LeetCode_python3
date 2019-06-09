# coding:utf-8

"""
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
    which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
    IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

    题目地址：https://leetcode.com/problems/integer-to-roman/

    Date: 2019/06/09
    By: Fargo
    Difficulty: Medium
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        # 范围[1, 3999]
        # 千位
        Roman = (num // 1000) * 'M'

        #
        list_roman = ['M', 'D', 'C', 'C', 'L', 'X', 'X', 'V', 'I']
        num_m = str(num % 1000 // 100) + str(num % 100 // 10) + str(num % 10)

        for i in range(len(num_m)):
            m = int(num_m[i])
            if m == 9:
                Roman = Roman + list_roman[i * 3 + 2] + list_roman[i * 3]
            elif m < 9 and m > 5:
                Roman = Roman + list_roman[i * 3 + 1] + (m-5) * list_roman[i * 3 + 2]
            elif m == 5:
                Roman = Roman + list_roman[i * 3 + 1]
            elif m == 4:
                Roman = Roman + list_roman[i * 3 + 2] + list_roman[i * 3 + 1]
            else:
                Roman = Roman + m * list_roman[i * 3 + 2]

        return Roman


print(Solution().intToRoman(58))

