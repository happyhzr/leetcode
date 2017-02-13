package main

import "fmt"

func main() {
	//nums := []int{2, 3, 1, 1, 4}
	nums := []int{1, 0, 2}
	result := canJump(nums)
	fmt.Println(result)
}

func canJump(nums []int) bool {
	last := len(nums) - 1
	for i := last - 1; i >= 0; i-- {
		if i + nums[i] >= last {
			last = i
		}
	}
	return last == 0
}
