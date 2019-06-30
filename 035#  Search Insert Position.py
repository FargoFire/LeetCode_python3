# coding:utf-8

"""
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where
    it would be if it were inserted in order.
    You may assume no duplicates in the array.

    Example 1:   Input: [1,3,5,6], 5   Output: 2

    题目地址：https://leetcode.com/problems/search-insert-position/

    Date: 2019/06/28
    By: Fargo
    Difficulty: Easy
"""
import time
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left


start = time.clock()
nums = [1,2,3,5,6,7,9,11,23,56,67,71]
out = Solution().searchInsert(nums, 73)
print(out, time.clock()-start)



