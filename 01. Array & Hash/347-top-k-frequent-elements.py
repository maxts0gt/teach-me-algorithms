# Leetcode 347

# Given an intereger array nums and 
# an integer k, return the k most frequent elements


from typing import List

# Time -> O(n)

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # first we create the hashmap
    hash = {}
    # and the we create array of arrays to count the each occurrence
    freq = [[] for i in range(len(nums) + 1)]
    # now let's go through the numbers
    for num in nums:
        # check if the num is hashmap
        # if exists then increase by 1 else by 0
        hash[num] = 1 + hash.get(num, 0)
    # now we go through the count we created
    # goal is basically attach them to the array of array we created earlier
    # so we grab the number and count together
    for number, count in hash.items():
        # now map the count to the number
        # if 1 is three times repeated, it will be 3 - 1
        # basically at index 3, the number '1' is attached
        freq[count].append(number)
    # now we are done with that, let's go through the list from top to down
    # cut it at the K-th size
    result = []
    for index in range(len(freq) - 1, 0, -1):
        # at each of that index bc some might have more than one number
        for number in freq[index]:
            # put the number in the result we created earlier
            result.append(number)
            # once the length of result is equal to K
            if len(result) == k:
                # then return the result
                return result
    # at some point it will return, so we don't have to return at the end.
    # Voila!


# Testing
nums = [1, 1, 1, 2, 2, 100, 6, 6, 6, 100, 100]
k = 3
print(topKFrequent(nums, k)) 