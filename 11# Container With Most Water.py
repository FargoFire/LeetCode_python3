# coding:utf-8

"""
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
    lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
    with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    题目地址：https://leetcode.com/problems/container-with-most-water/

    Date: 2019/06/08
    By: Fargo
    Difficulty: Medium
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        max_area = 0
        i, j = 0, n-1

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if max_area < area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

