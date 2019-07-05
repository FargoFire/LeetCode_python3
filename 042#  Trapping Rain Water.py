# coding:utf-8

"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
    water it is able to trap after raining.
    The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (
    blue section) are being trapped. Thanks Marcos for contributing this image!

    Example:  Input: [0,1,0,2,1,0,1,3,2,1,2,1]  Output: 6

    题目地址：https://leetcode.com/problems/trapping-rain-water/

    Date: 2019/07/05
    By: Fargo
    Difficulty: Hard
"""
import time
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        area = 0

        while left <= right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                    left += 1
                else:
                    area += left_max - height[left]
                    left += 1
            if height[left] >= height[right]:
                if height[right] >= right_max:
                    right_max = height[right]
                    right -= 1
                else:
                    area += right_max - height[right]
                    right -= 1
        return area


start = time.clock()
nums = [0,1,0,2,1,0,1,3,2,1,2,1]
out = Solution().trap(nums)
print(out, time.clock()-start)



