# coding:utf-8

"""
    The count-and-say sequence is the sequence of integers with the first five terms as following:
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
    Note: Each term of the sequence of integers will be represented as a string.

    Example 1: Input: 4  Output: "1211"

    题目地址：https://leetcode.com/problems/count-and-say/

    Date: 2019/07/01
    By: Fargo
    Difficulty: Easy
"""
import time


class Solution:
    def countAndSay(self, n: int) -> str:

        # s = '1'
        # for i in range(n-1):
        #     count = 0
        #     tmp = ''
        #     let = s[0]
        #     for l in s:
        #         if let == l:
        #             count +=1
        #         else:
        #             tmp += str(count) + let
        #             count = 1

        if n == 1:
            return '1'

        s = '11'
        for i in range(1, n-1):
            count = 1
            tmp = ''
            for j in range(len(s)):
                if j != len(s)-1:
                    if s[j] == s[j+1]:
                        count += 1
                    else:
                        tmp += str(count) + s[j]
                        count = 1
                else:
                    tmp += str(count) + s[j]
            s = tmp

        return s


start = time.clock()
n = 2
out = Solution().countAndSay(n)
print(out, time.clock()-start)



