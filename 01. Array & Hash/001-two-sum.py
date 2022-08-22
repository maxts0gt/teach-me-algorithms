#  Leetcode 1

# Given an array of integers, 
# return indices of the two numbers such that
# they add up to a specific target


# Time -> O(n)
# Space -> O(n)

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # create hash map for storing value
    prevMap = {} #val : index
    # now go through the list of nums
    # but we need the both index and number
    for i, n in enumerate(nums):
        # now we find out the difference
        diff = target - n
        # and see if that difference is in our hash
        if diff in prevMap:
            # if it's inside our hash map
            # then return the index of diff and current number
            return [prevMap[diff], i]
        # else we just update the hashmap
        prevMap[n] = i
    # and if nothing, there just return. Voila!
    return


# Testing
nums = [2, 1, 5, 3]
target = 6
print(twoSum(nums, target))