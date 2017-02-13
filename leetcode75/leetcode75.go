package leetcode75

func sortColors(nums []int) {
	start0 := 0
	start1 := sortColor(nums, start0, 0)
	sortColor(nums, start1, 1)
}

func sortColor(nums []int, start int, target int) int {
	i, j := start, start
	for i < len(nums) {
		if nums[i] == target {
			swap(nums, i, j)
			i++
			j++
		} else {
			i++
		}
	}
	return j
}

func swap(nums []int, i int, j int) {
	if i == j {
		return
	}
	nums[i], nums[j] = nums[j], nums[i]
}
