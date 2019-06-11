# coding:utf-8

"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    题目地址：https://leetcode.com/problems/longest-common-prefix/

    Date: 2019/06/11
    By: Fargo
    Difficulty: Easy
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 公共前缀字符串
        str_i = ''

        if len(strs) == 1:
            str_i = strs[0]

        for i in range(len(strs)-1):
            range_j = min(len(strs[i]), len(strs[i+1]))
            str_i = ''
            for j in range(range_j):
                if strs[i][j] == strs[i+1][j]:
                    str_i = str_i + strs[i][j]
                else:
                    break
            strs[i+1] = str_i

        return str_i
    

print(Solution().longestCommonPrefix(["a"]))

