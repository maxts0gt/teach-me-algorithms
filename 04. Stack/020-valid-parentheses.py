# Leetcode 020

# Given a string s containing just the characters
#  '(',  ')', '{', '}', '[', ']',
# determine if the string is valid

# Time -> O(n)
# Space -> O(n)

def validParentheses(input: str) -> bool:
    # we need an array to store 
    stack = []
    # we will create hash since we know the values
    closeToOpen = {')': '(',']': '[','}': '{'}
    # now we need to go through the input
    for value in input:
        # then we check if we have that value in closeToOpen
        if value in closeToOpen:
            # we do some magic here if it exists
            # basically check if there is something in stack
            # and stack's last value is equal to one it has inside closeToOpen
            if stack and stack[-1] == closeToOpen[value]:
                # now we pop it from the stack
                # so it is not stored there anymore
                stack.pop()
        # else, meaning if we don't have it inside closeTopen
        # we know it's the opening value
        else:
            stack.append(value)
    # what comes here is important
    # we know that stack should be empty for this to be true
    return True if not stack else False





# Testing
input1 = "(]"
input2 = "()[]{}"
print(validParentheses(input1))
print(validParentheses(input2))