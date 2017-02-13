package leetcode74

func searchMatrix(matrix [][]int, target int) bool {
	nRow := len(matrix)
	if nRow == 0 {
		return false
	}
	nCol := len(matrix[0])
	low := 0
	high := nRow * nCol - 1

	for low <= high {
		mid := low + (high - low) / 2
		elem := getValue(matrix, mid)
		if elem == target {
			return true
		}
		if elem < target {
			low = mid + 1
		} else if elem > target {
			high = mid - 1
		}
	}

	return false
}

func getValue(matrix [][]int, index int) int {
	nCol := len(matrix[0])
	i := index / nCol
	j := index % nCol
	return matrix[i][j]
}
