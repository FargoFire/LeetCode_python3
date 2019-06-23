# coding:utf-8

"""
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
    extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    题目地址：https://leetcode.com/problems/remove-element/

    Date: 2019/06/22
    By: Fargo
    Difficulty: Easy
"""
import json
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[n] = nums[i]
                n += 1

        return n


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


nums = [2,2,2,2,2]
ret = Solution().removeElement(nums, 2)
out = integerListToString(nums,len_of_list=ret)
print(out)



