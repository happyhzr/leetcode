package leetcode66

func plusOne(digits []int) []int {
	var i int
	for i = len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i] += 1
			break
		} else if digits[i] == 9 {
			digits[i] = 0
		}
	}
	if i > -1 {
		return digits
	}
	newDigits := make([]int, len(digits) + 1)
	newDigits[0] = 1
	for i := 0; i < len(digits); i++ {
		newDigits[i + 1] = digits[0]
	}
	return newDigits
}
