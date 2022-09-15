// Leetcode 78

package main

func subsets(nums []int) [][]int {
	result := make([][]int, 0)
	subset := make([]int, 0)

	var dfs func(index int)
	dfs = func(index int) {
		result = append(result, append([]int{}, subset...))
		if index == len(nums) {
			return
		}
		for i := index; i < len(nums); i++ {
			subset = append(subset, nums[i])
			dfs(i + 1)
			subset = subset[:len(subset)-1]
		}
	}
	dfs(0)
	return result
}
