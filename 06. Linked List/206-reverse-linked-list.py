# Leetcode 206

# Time -> O(n)
# Space -> O(1)

def reverseLinkedList(head):
    # first set prev value to none
    # and current value to the head
    prev, curr = None, head

    # while we have value at curr
    while curr:
        # create next value 
        # for example, given [null -> 1 -> 2 ] basically "next" is "2"
        next = curr.next
        # current's next value is None
        curr.next = prev
        # prev value to 1
        prev = curr
        # current value to 2
        # now list is: prev [2]
        curr = next
    return prev
    




# Testing
input = [1, 2, 3, 4, 5, 6]
print(reverseLinkedList(input))