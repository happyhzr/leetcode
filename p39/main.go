package p39

func combinationSum(candidates []int, target int) [][]int {
	coms := [][]int{}
	com := []int{}
	dfs(candidates, target, &coms, &com, 0)
	return coms
}

func dfs(candidates []int, target int, coms *[][]int, com *[]int, i int) {
	if i == len(candidates) {
		return
	}
	if target == 0 {
		cp := make([]int, len(*com))
		copy(cp, *com)
		*coms = append(*coms, cp)
		return
	}
	dfs(candidates, target, coms, com, i+1)
	if candidates[i] <= target {
		*com = append(*com, candidates[i])
		dfs(candidates, target-candidates[i], coms, com, i)
		*com = (*com)[:len(*com)-1]
	}
}
