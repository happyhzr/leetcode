package leetcode33

func search(nums []int, target int) int {
	l := len(nums)
	if l == 0 {
		return -1
	}

	rotate := findSmallest(nums)
	low, high := 0, l-1
	var mid, realmid int
	for low <= high {
		mid = (low + high) / 2
		realmid = (mid + rotate) % l
		if nums[realmid] == target {
			return realmid
		}
		if nums[realmid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

func findSmallest(nums []int) int {
	low := 0
	high := len(nums) - 1
	var mid int
	for low < high {
		mid = (low + high) / 2
		//nums[mid] never equal nums[high]
		if nums[mid] < nums[high] {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return high
}
