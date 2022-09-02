package heap

type KthLargest struct {
	k   int
	arr []int
}

func heapify(arr []int, index, size int) {
	left := (index << 1) + 1
	root := index
	right := left + 1
	if left < size && arr[left] < arr[root] {
		root = left
	}
	if right < size && arr[right] < arr[root] {
		root = right
	}
	if root != index {
		arr[root], arr[index] = arr[index], arr[root]
		heapify(arr, root, size)
	}
}

func Constructor(k int, nums []int) KthLargest {
	arr := make([]int, k)
	for i := len(nums); i < k; i++ {
		nums = append(nums, -100001)
	}
	for i := 0; i < k; i++ {
		arr[i] = nums[i]
	}
	for i := k >> 1; i >= 0; i-- {
		heapify(arr, i, k)
	}
	for i := len(nums) - 1; i >= k; i-- {
		if arr[0] < nums[i] {
			arr[0] = nums[i]
			heapify(arr, 0, k)
		}
	}
	return KthLargest{k, arr}
}

func (largest *KthLargest) Add(val int) int {
	if val > largest.arr[0] {
		largest.arr[0] = val
		heapify(largest.arr, 0, largest.k)
	}
	return largest.arr[0]
}
