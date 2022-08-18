# Leetcode 217

# Given an integer array nums, 
# return true if any value appears 
# at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(nums) -> bool:
    # basically we create a hashset
        hashset = set()
        # then loop through the numbers
        for n in nums:
            # while looping, we check if the number is
            # in the hashset 
            if n in hashset:
                # if it is there, we return true
                return True 
            # after checking the number in hashset
            # meaning loop is still running which means number isn't there
            # we add the next number into the hashset
            # it loops again and again till the end
            hashset.add(n)
        # if loop exits, it means there is none
        # so we return false
        return False

nums = [1, 3, 2, 1]
print(containsDuplicate(nums))