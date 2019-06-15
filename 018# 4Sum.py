# coding:utf-8

"""
    Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
    a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

    Note:  The solution set must not contain duplicate quadruplets.

    Example: Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]

    题目地址：https://leetcode.com/problems/4sum/

    Date: 2019/06/15
    By: Fargo
    Difficulty: Medium
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        nums = sorted(nums)
        for i in range(len(nums)-3):
            if nums[i-1] == nums[i] and i > 0:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[j-1] == nums[j] and j > i+1:
                    continue
                diff = target - nums[i] - nums[j]
                index_l = j+1
                index_r = len(nums)-1
                while index_l < index_r:
                    if nums[index_l] + nums[index_r] == diff:
                        res.append([nums[i], nums[j], nums[index_l], nums[index_r]])
                        index_l +=1
                        index_r -=1
                        while index_l < index_r and nums[index_l] == nums[index_l-1]:
                            index_l +=1
                        while index_l < index_r and nums[index_r] == nums[index_r+1]:
                            index_r -=1
                    elif nums[index_l] + nums[index_r] < diff:
                        index_l +=1
                    else:
                        index_r -=1
        return res


print(Solution().fourSum([0,0,0,0], 0))

