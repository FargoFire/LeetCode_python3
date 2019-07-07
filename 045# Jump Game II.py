# coding:utf-8

"""
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Your goal is to reach the last index in the minimum number of jumps.

    题目地址：https://leetcode.com/problems/jump-game-ii/

    Date: 2019/07/07
    By: Fargo
    Difficulty: Hard
"""
import time
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return 0

        n, jump_f, jump_t, nxt = 1, 0, nums[0], 0
        while jump_t < len(nums)-1:
            n += 1
            for i in range(jump_f, jump_t+1):
                jump = i + nums[i]
                nxt = max(nxt, jump)
            jump_f = jump_t
            jump_t = nxt

        return n


start = time.clock()
num = [2,2,3,4]
out = Solution().jump(num)
print(out, time.clock()-start)



