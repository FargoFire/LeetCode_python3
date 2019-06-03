# coding:utf-8

"""
    Given a string, find the length of the longest substring without repeating characters.
    找出不重复的最长子字符串
    Example 1:
    Input: "abcabcbb"
    Output: 3         Explanation: The answer is "abc", with the length of 3.

    题目地址： https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Date： 2019/06/02
    By: Fargo
    Level: Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0
        m = []
        n, i, j = len(s), 0, 0

        while i < n and j < n:
            if s[j] in m:
                m.remove(s[i])
                i += 1
            else:
                m.append(s[j])
                max_num = max(max_num, len(m))
                j += 1

        return max_num


print(Solution().lengthOfLongestSubstring("bbtablud"))


# 以下是最初思路，但耗时过长
# for j in range(len(s)):
#     for i in range(len(s)):
#         m.append(s[i])
#
#         if (i + 1) < len(s):
#             a = s[i + 1]
#             if a not in m:
#                 continue
#             if len(m) > max_num:
#                 max_num = len(m)
#             m = []
#         else:
#             if len(m) > max_num:
#                 max_num = len(m)
#             m = []
#     s = s[1:]
# return max_num



