# coding:utf-8

"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    For example, given n = 3, a solution set is:
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

    题目地址：https://leetcode.com/problems/generate-parentheses/

    Date: 2019/06/19
    By: Fargo
    Difficulty: Medium
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parentheses_list = []

        def Backtracking(parentheses='', left=0, right=0):
            if len(parentheses) == 2*n:
                parentheses_list.append(parentheses)
                return
            if left < n:
                Backtracking(parentheses+'(', left+1, right)
            if right < left:
                Backtracking(parentheses+')', left, right+1)

        Backtracking()
        return parentheses_list


print(Solution().generateParenthesis(3))

