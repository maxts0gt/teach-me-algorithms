# Leetcode 704

# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# Time -> O(log n)

from typing import List


def binarySearch(nums: List[int], target: int) -> int:
    # basically we are gonna use two pointers
    # one starting at 0 and other starting at the end
    left, right = 0, len(nums) - 1
    # while left is lower or equal to right
    # meaning that left and right hasn't met yet
    while left <= right:
        # we will find out the middle first (say we have 10 in the list)
        # middle is (10 - 1) / 2 + 1 or 6 on the next
        middle = left + ((right - left) // 2)
        # then we check if the middle is higher than target
        if nums[middle] > target:
            # we update the right to the mid
            right = middle - 1
        # if the middle is lower than target then we move the left
        elif nums[middle] < target:
            left = middle + 1
        # else meaning we got it or it is equal to target
        else: 
            # we return the middle
            return middle
    # if not, we just return the -1
    return -1




# Testing

nums = [1,2,3,4,5,6,7,8,9,10]; targetOne = 9; targetTwo = 2
print(binarySearch(nums, targetOne))
# print(binarySearch(nums, targetTwo))