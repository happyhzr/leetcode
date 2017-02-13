package main

import (
	"fmt"
)

func main() {
	x := 34.00515
	n := -3
	res := myPow(x, n)
	fmt.Println(res)
}

func myPow(x float64, n int) float64 {
	if n == 0 {
		return 1.0
	}
	if n < 0 {
		n = -n
		x = 1.0 / x
	}
	ans := 1.0
	for n > 0 {
		if n & 1 == 1 {
			ans *= x
		}
		x *= x
		n >>= 1
	}
	return ans
}
