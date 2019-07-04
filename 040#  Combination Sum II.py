# coding:utf-8

"""
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
    in candidates where the candidate numbers sums to target.
    Each number in candidates may only be used once in the combination.
    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

    题目地址：https://leetcode.com/problems/combination-sum-ii/

    Date: 2019/07/03
    By: Fargo
    Difficulty: Medium
"""
import time
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def Recurve(candidates, target, res, list):
            for i in range(len(candidates)):
                if target < candidates[i]:
                    break
                elif target == candidates[i]:
                    if candidates[i] == candidates[i - 1] and i > 0:
                        continue
                    else:
                        res.append(list + [target])
                else:
                    if candidates[i] == candidates[i - 1] and i > 0:
                        continue
                    else:
                        Recurve(candidates[i+1:], target-candidates[i], res, list+[candidates[i]])

        candidates = sorted(candidates)
        res = []
        Recurve(candidates, target, res, [])
        return res


start = time.clock()
candidates = [2,2]
target = 4
out = Solution().combinationSum2(candidates, target)
print(out, time.clock()-start)



