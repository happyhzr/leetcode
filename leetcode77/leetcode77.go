package leetcode77

import "fmt"

func combine(n int, k int) [][]int {
	if k > n {
		k = n
	}
	max := getCount(n, k)
	fmt.Println(max)
	combinations := make([][]int, 0, max)
	combination := make([]int, n)
	for i := 0; i < n; i++ {
		combination[i] = i + 1
	}

	dfs(combinations, combination, n, k, 0)
	return combinations
}

func dfs(combinations [][]int, combination []int, n int, k int, deep int) {
	if deep == k {
		fmt.Println(combination)
		dup := make([]int, k)
		copy(dup, combination[:k])
		combinations = append(combinations, dup)
		return
	}

	for i := deep; i < n; i++ {
		combination[i], combination[deep] = combination[deep], combination[i]
		dfs(combinations, combination, n, k, deep + 1)
		combination[i], combination[deep] = combination[deep], combination[i]
	}
}

func getCount(n int, k int) int {
	mul := 1
	for i := n; i >= n - k + 1; i-- {
		mul *= i
	}
	return mul
}
