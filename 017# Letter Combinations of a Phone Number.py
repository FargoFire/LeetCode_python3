# coding:utf-8

"""
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
    could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
    any letters.

    Example:  Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    Note: Although the above answer is in lexicographical order, your answer could be in any order you want.

    题目地址：https://leetcode.com/problems/letter-combinations-of-a-phone-number/

    Date: 2019/06/14
    By: Fargo
    Difficulty: Medium
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # 回溯法
        def Backletter(letter, digits):
            if len(digits) == 0:
                letter_list.append(letter)
            else:
                for letter_ in phone[digits[0]]:
                    Backletter(letter + letter_, digits[1:])

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        letter_list = []
        if digits:
            Backletter('', digits)

        return letter_list


print(Solution().letterCombinations("23"))

