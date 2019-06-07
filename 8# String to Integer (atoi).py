# coding:utf-8

"""
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first non-whitespace character
    is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many
    numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and
    have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
    exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:
    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1)
    or INT_MIN (−231) is returned.

    题目地址：https://leetcode.com/problems/string-to-integer-atoi/

    Date: 2019/06/06
    By: Fargo
    Difficulty: Medium
"""
import math

class Solution:
    def myAtoi(self, str: str) -> int:

        new_str = ''
        int_max = int(math.pow(2, 31) - 1)
        int_min = int(-1 * math.pow(2, 31))
        numbers = ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+']
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        str = str.lstrip()

        if len(str) > 0 and str[0] in numbers:
            new_str = new_str + str[0]
            for i in range(1, len(str)):
                if str[i] in number:
                    new_str = new_str + str[i]
                else:
                    break
        else:
            return 0

        if new_str != '-' and new_str != '+':
            # range[−2^31,  2^31 − 1]
            if int(new_str) > int_max:
                return int_max
            if int(new_str) < int_min:
                return int_min
            else:
                return int(new_str)
        else:
            return 0


print(Solution().myAtoi("   +0 123"))

