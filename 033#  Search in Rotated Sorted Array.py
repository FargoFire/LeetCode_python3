# coding:utf-8

"""
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.
    Your algorithm's runtime complexity must be in the order of O(log n).

    Example 1: Input: nums = [4,5,6,7,0,1,2], target = 0  Output: 4

    题目地址：https://leetcode.com/problems/search-in-rotated-sorted-array/

    Date: 2019/06/26
    By: Fargo
    Difficulty: Medium
"""
import time
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums) - 1
        left = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


start = time.clock()
nums = [4,5,6,7,8,0,1,2]
out = Solution().search(nums, 3)
print(out, time.clock()-start)



