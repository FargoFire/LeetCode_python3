# coding:utf-8

"""
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
    1 Open brackets must be closed by the same type of brackets.
    2 Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    题目地址：https://leetcode.com/problems/valid-parentheses/

    Date: 2019/06/17
    By: Fargo
    Difficulty: Easy
"""

class Solution:
    def isValid(self, s: str) -> bool:

        # 1 堆栈
        stack = []
        brackets_dict = {')': '(', ']': '[', '}': '{',}

        for bracket in s:
            if bracket in brackets_dict:
                if stack:
                    ss = stack.pop()
                else:
                    ss = ''

                if ss != brackets_dict[bracket]:
                    return False
            else:
                stack.append(bracket)

        if not stack:

            return True
        else:
            return False


print(Solution().isValid("]"))

