package main

import (
	"fmt"
	"sort"
)

func main() {
	candidates := []int{1} //{10, 1, 2, 7, 6, 1, 5}
	fmt.Println(candidates)
	target := 1 //8
	results := combinationSum2(candidates, target)
	fmt.Println(results)
}

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	results := [][]int{}
	result := []int{}
	dfs(candidates, target, &result, &results, 0)
	return results
}

func dfs(candidates []int, target int, result *[]int, results *[][]int, index int) {
	if target < 0 {
		return
	}
	if target == 0 {
		*results = append(*results, *result)
		return
	}
	for i := index; i < len(candidates); i++ {
		if i > index && i < len(candidates) && candidates[i-1] == candidates[i] {
			continue
		}
		v := candidates[i]
		if target < v {
			break
		}
		dup := make([]int, len(*result))
		copy(dup, *result)
		dup = append(dup, v)
		dfs(candidates, target-v, &dup, results, i+1)
	}
}
