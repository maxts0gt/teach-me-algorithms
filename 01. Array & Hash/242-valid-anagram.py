# Leetcode 242

# Given two strings s and t, 
# return true if t is an anagram of s, 
# and false otherwise.

def isAnagram(s: str, t:str) -> bool:
    # before we even start
    # we should check if the length is equal
    if len(s) != len(t):
        # if it is not equal just return false
        return False
    # we will counting the letters in the hashmap
    # so, create two hashmaps
    countS, countT = {}, {}
    # loop through the "s"
    for i in range(len(s)):
        # grab the put it inside the hash
        # and everytime you see "s" add 1 to it else add 0
        countS[s[i]] = 1 + countS.get(s[i], 0)
        # do same for the "t"
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # now loop through the countS
    for c in countS:
        # check if the letter we grab from S
        # has the same value as the T
        if countS[c] != countT.get(c, 0):
            # if not, return False
            return False
    # if we did't return false and quit the loop, then return True
    return True




s1 = "rat"; t1 = "car"
s2 = "anagram"; t2 = "naagram"
print(isAnagram(s1, t1))
print(isAnagram(s2, t2))