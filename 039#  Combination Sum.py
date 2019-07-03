# coding:utf-8

"""
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
    combinations in candidates where the candidate numbers sums to target.
    The same repeated number may be chosen from candidates unlimited number of times.

    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    Example 1:
    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]

    题目地址：https://leetcode.com/problems/combination-sum/

    Date: 2019/07/02
    By: Fargo
    Difficulty: Medium
"""
import time
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def Recurve(candidates, target, res, list):
            for i in range(len(candidates)):
                if target < candidates[i]:
                    break
                elif target == candidates[i]:
                    res.append(list+[target])
                else:
                    Recurve(candidates[i:], target-candidates[i], res, list+[candidates[i]])

        candidates = sorted(candidates)
        res = []
        Recurve(candidates, target, res, [])
        return res


start = time.clock()
candidates = [8,2,3,6,7]
target = 7
out = Solution().combinationSum(candidates, target)
print(out, time.clock()-start)



