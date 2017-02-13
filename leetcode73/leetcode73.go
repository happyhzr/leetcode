package leetcode73

func setZeroes(matrix [][]int) {
	row := len(matrix)
	if row == 0 {
		return
	}

	col := len(matrix[0])
	rowMark := make([]bool, row)
	colMark := make([]bool, col)

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if matrix[i][j] != 0 {
				continue
			}
			if !rowMark[i] {
				rowMark[i] = true
			}
			if !colMark[j] {
				colMark[j] = true
			}
		}
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if rowMark[i] || colMark[j] {
				matrix[i][j] = 0
			}
		}
	}
}

func copyMatrix(matrix [][]int) [][]int {
	row := len(matrix)
	cop := make([][]int, row)
	for i := 0; i < row; i++ {
		col := len(matrix[i])
		cop[i] = make([]int, col)
		copy(cop[i], matrix[i])
	}
	return cop
}
