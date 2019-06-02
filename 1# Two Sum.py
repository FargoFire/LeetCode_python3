# coding:utf-8

"""
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    题目地址：https://leetcode.com/problems/two-sum/

    Date: 2019/06/01
    By: Fargo
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1.
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i, j]

        # 2.
        for i in range(len(nums)):
            a = target - nums.pop(0)
            if a in nums:
                j = nums.index(a) + i + 1
                return [i, j]

