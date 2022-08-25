#  Leetcode 1

# Give a string, find the length of
# longest substring without repeating chars


# Time -> O(n)
# Space -> O(n)

def longestSubstring(strings: str) -> int:
    # we need a simple set
    # set doesn't restore same value twice
    hash = set()
    # we need a left pointer
    left = 0
    # we need result variable to store result
    result = 0
    # now we go through the input variable, so simple loop
    for right in range(len(strings)):
        # now check if the char in the hash
        while strings[right] in hash:
            # if it exists, then remove that hash from left
            # you may have wondered why while not simple if 
            # because we want to remove it till we don't have it anymore
            hash.remove(strings[left])
            # and keep moving the left towards right
            left += 1
        # after the while loop we want to add the next right char
        hash.add(strings[right])
        # and update result variable which will return at the end
        result = max(result, right - left + 1)
    # Voila! 
    return result



# Testing
str = "abcabcbbdaserq"
print(longestSubstring(str))