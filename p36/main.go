package p36

func isValidSudoku(board [][]byte) bool {
	rows := make([][]int, 10)
	for i := range rows {
		rows[i] = make([]int, 10)
	}
	cols := make([][]int, 10)
	for i := range cols {
		cols[i] = make([]int, 10)
	}
	boxes := make([][][]int, 3)
	for i := range boxes {
		boxes[i] = make([][]int, 3)
		for j := range boxes[i] {
			boxes[i][j] = make([]int, 10)
		}
	}

	for i, row := range board {
		for j, v := range row {
			if v == '.' {
				continue
			}
			c := v - '0'
			rows[i][c]++
			cols[j][c]++
			boxes[i/3][j/3][c]++
			if rows[i][c] > 1 || cols[j][c] > 1 || boxes[i/3][j/3][c] > 1 {
				return false
			}
		}
	}
	return true
}
