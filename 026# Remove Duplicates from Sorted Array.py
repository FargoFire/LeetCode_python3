# coding:utf-8

"""
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once
    and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with
    O(1) extra memory.

    题目地址：https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Date: 2019/06/21
    By: Fargo
    Difficulty: Easy
"""
import json
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[n]:
                n += 1
                nums[n] = nums[i]
        return n


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


nums = [1, 1, 2, 3, 6, 8, 8, 3, 2, 3, 2]
ret = Solution().removeDuplicates(nums)
out = integerListToString(nums,len_of_list=ret)
print(out)



