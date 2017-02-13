package leetcode69

func mySqrt(x int) int {
	if x == 0 || x == 1 {
		return x
	}

	low, high := 1, x
	for {
		if high - low == 1 {
			return low
		}
		mid := low + (high - low) / 2;
		if mid * mid == x {
			return mid
		}
		if mid * mid < x {
			low, high = mid, high
		} else {
			low, high = low, mid
		}
	}
}