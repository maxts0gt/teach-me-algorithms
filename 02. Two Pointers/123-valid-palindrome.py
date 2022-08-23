# Leetcode 125

# Given a string s, determine if it is a palindrome
# considering only alphanumeric characters and ignoring cases

def validPalindrome(s: str) -> bool: 
    # our strategy is to create two pointer
    # start from two side and keep comparing till the mid
    left, right = 0, len(s) - 1
    # now while left is right, we loop
    while left < right:
        # and also use our helper function to check alphaNum
        # what we are doing is basically
        # check if we are still not in the mid
        # and the char is not true then skip the current
        while left < right and not alphaNum(s[left]):
            left += 1
        # same for the right side pointer
        while right > left and not alphaNum(s[right]):
            right -= 1
        # here our comparing logic comes in
        # basically check if the left and right not equal
        if s[left].lower() != s[right].lower():
            return False
        # and move the pointers to the mid
        left, right = left + 1, right - 1
    return True

# we will need helper function
# to check if the str is only alphanumeric
def alphaNum(char):
    return (ord('A') <= ord(char) <= ord("Z") or 
    ord('a') <= ord(char) <= ord("z") or 
    ord('0') <= ord(char) <= ord("9")) 



# Testing
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"

print('s1', validPalindrome(s1))
print('s2', validPalindrome(s2))