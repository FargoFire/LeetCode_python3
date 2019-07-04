# coding:utf-8

"""
    Given an unsorted integer array, find the smallest missing positive integer.

    Example 1: Input: [1,2,0] Output: 3
    Example 2: Input: [3,4,-1,1] Output: 2

    Note:  Your algorithm should run in O(n) time and uses constant extra space.

    题目地址：https://leetcode.com/problems/first-missing-positive/

    Date: 2019/07/04
    By: Fargo
    Difficulty: Hard
"""
import time
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = sorted(nums)
        add = 1
        for i in range(len(nums)):
            if nums[i] < 1:
                continue
            elif nums[i] == nums[i-1] and i > 0:
                continue
            else:
                if nums[i] == add:
                    add += 1
                else:
                    return add
        return add


start = time.clock()
nums = [1]
out = Solution().firstMissingPositive(nums)
print(out, time.clock()-start)



