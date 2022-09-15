# Leetcode 78

# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

from typing import List


def subsets(nums: List[int]) -> List[int]:
    result = []
    subset = []

    def dfs(i): 
        if i >= len(nums):
            result.append(subset.copy())
            return
        # decision to include
        subset.append(nums[i])
        dfs(i + 1)
        # decision to not include
        subset.pop()
        dfs(i + 1)
    
    dfs(0)
    return result


# Testing
nums = [1,2,3]
print(subsets(nums))