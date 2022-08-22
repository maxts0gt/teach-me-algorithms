# Leetcode 49

# Given an array of strings "strs", 
# group the anagrams together

# Time -> O(m * n)

from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # create a hashmap to list anagrams (with dict values)
    hashMap = defaultdict(list)
    # basically we will go through the strings
    # check them one by one
    for s in strs:
        # initialize count arrays, so will we have 26 zero arrays
        count = [0] * 26 # a ... z
        # go through the every single characters
        for c in s: 
            # then we will map each value to the arrays
            # by incrementing each value when it appears
            count[ord(c) - ord("a")] += 1
        # right after the inner loop
        # now we are grouping the anagrams together
        hashMap[tuple(count)].append(s)
    # and then we just need to return the values from the hashmap
    # voila!
    return hashMap.values()



# Testing
strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(groupAnagrams(strs))