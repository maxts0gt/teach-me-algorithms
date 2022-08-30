# Leetcode 226

def invertBinaryTree(root): 
    # check if the root is not empty
    if not root:
        # if empty we return early
        return None
    # keep root.left value in temp value
    tmp = root.left
    # keep root.right in root.left
    root.left = root.right
    # and tmp value to root.right
    # so we are basically swapping it
    root.right = tmp
    # now call itself on every left
    invertBinaryTree(root.left)
    # now call itself on every right
    invertBinaryTree(root.right)
    # and return root. Voila!
    return root
