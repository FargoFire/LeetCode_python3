# coding:utf-8

"""
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
    parentheses substring.

    Example 1:
    Input: "(()"    Output: 2
    Explanation: The longest valid parentheses substring is "()"

    题目地址：https://leetcode.com/problems/longest-valid-parentheses/

    Date: 2019/06/25
    By: Fargo
    Difficulty: Hard
"""
import time


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        #  Kanac 的 算法
        # max_lenght = 0
        # stack = [0]
        # for c in s:
        #     if c == '(':
        #         stack.append(0)
        #     else:
        #         if len(stack) > 1:
        #             p = stack.pop()
        #             stack[-1] += p + 2
        #             max_lenght = max(max_lenght, stack[-1])
        #         else:
        #             stack = [0]
        # return max_lenght

        # 不够简洁， 如stack = [0, 2, 9]
        max_lenght, n = 0, 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > n:
                    stack.pop()
                else:
                    n += 1
                    stack.append(i)

        stack.insert(0, 0)
        stack.append(len(s))
        print(stack)
        for i in range(1, len(stack)):
            if i == 1:
                max_lenght = max(max_lenght, stack[i] - stack[0])
            else:
                max_lenght = max(max_lenght, stack[i] - stack[i-1] - 1)

        return max_lenght


start = time.clock()
parentheses = "(()((()))"
out = Solution().longestValidParentheses(parentheses)
print(out, time.clock()-start)



