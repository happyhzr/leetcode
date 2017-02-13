package main

import (
	"fmt"
	"sort"
)

func main() {
	c := []int{7, 3, 2}
	t := 18
	results := combinationSum(c, t)
	fmt.Println(results)
}

func combinationSum(candidates []int, target int) [][]int {
	var results [][]int
	sort.Ints(candidates)
	//fmt.Println(candidates)
	dfs(candidates, target, 0, []int{}, &results)
	return results
}

func dfs(candidates []int, target int, start int, result []int, results *[][]int) {
	//fmt.Println(target)
	if target == 0 {
		*results = append(*results, result)
		//fmt.Println(result)
		//fmt.Println(results)
		return
	}
	for i := start; i < len(candidates); i++ {
		v := candidates[i]
		if v <= target {
			var sl = make([]int, len(result))
			copy(sl, result)
			//sl := result
			sl = append(sl, v)
			//fmt.Println(sl)
			dfs(candidates, target-v, i, sl, results)
		} else {
			break
		}
	}
}
