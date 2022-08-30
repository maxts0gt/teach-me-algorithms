// Leetcode 226

func invertBinaryTree(root *TreeNode) *TreeNode {
	// check if the root is nil
	if root == nil {
		// if so return early
		return root
	}

	// assign root.Left values to left
	left := invertBinaryTree(root.Left)
	// assign root.Right values to root.Left
	root.Left = invertBinaryTree(root.Right)
	// and finally assign the left values to root.Right
	root.Right = left

	return root
}