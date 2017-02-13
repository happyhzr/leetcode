package main

import "fmt"

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	arr := spiralOrder(matrix)
	fmt.Println(arr)
}

const (
	RIGHT = iota
	DOWN
	LEFT
	UP
)

func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}

	n := len(matrix)
	m := len(matrix[0])
	mat := make([][]bool, n)
	for i := 0; i < n; i++ {
		mat[i] = make([]bool, m)
	}
	arr := make([]int, n * m)
	move := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	i, j, k := 0, 0, 0
	status := RIGHT

	for true {
		arr[k] = matrix[i][j]
		mat[i][j] = true
		k++

		newi := i + move[status][0]
		newj := j + move[status][1]
		if isMovable(newi, newj, n, m, mat) {
			i, j = newi, newj

		} else {
			status = nextStatus(status)
			newi = i + move[status][0]
			newj = j + move[status][1]
			if isMovable(newi, newj, n, m, mat) {
				i, j = newi, newj
			} else {
				break
			}
		}
	}
	return arr;
}

func isMovable(i, j, n, m int, mat [][]bool) bool {
	if i >= 0&&i <= n - 1&&j >= 0&&j <= m - 1&&mat[i][j] == false {
		return true
	}
	return false
}

func nextStatus(status int) int {
	if status == UP {
		status = RIGHT
	} else {
		status++
	}
	return status
}