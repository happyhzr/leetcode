package leetcode52

func totalNQueens(n int) int {
	vector := make([]int, n)
	count := 0
	search(vector, n, &count, 0)
	return count
}

func search(vector []int, n int, count *int, row int) {
	if row >= n {
		*count++
		return
	}
	for col := 0; col < n; col++ {
		if isValid(vector, row, col) {
			vector[row] = col
			search(vector, n, count, row+1)
			vector[row] = -1
		}
	}
}

func isValid(vector []int, row int, col int) bool {
	for i := 0; i < row; i++ {
		if vector[i] == col {
			return false
		}
		dx := abs(vector[i] - col)
		dy := row - i
		if dx == dy {
			return false
		}
	}
	return true
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
