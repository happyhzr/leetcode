package main

import "fmt"

func main() {
	grid := [][]int{
		{1, 2},
		{3, 4},
	}
	minPath := minPathSum(grid)
	fmt.Println(minPath)

	a := "hello"
	b := "hello"
	fmt.Println(a == b)
}

func minPathSum(grid [][]int) int {
	row := len(grid)
	if row == 0 {
		return 0
	}
	col := len(grid[0])
	minPathGrid := newMinPathGrid(row, col)

	for i := row - 1; i >= 0; i-- {
		for j := col - 1; j >= 0; j-- {
			minPath := getNextMinPath(minPathGrid, i, j)
			minPathGrid[i][j] = minPath + grid[i][j]
		}
	}
	return minPathGrid[0][0]
}

func newMinPathGrid(row int, col int) [][]int {
	grid := make([][]int, row)
	for i := 0; i < row; i++ {
		grid[i] = make([]int, col)
	}
	return grid
}

func getNextMinPath(minPathGrid [][]int, i int, j int) int {
	row := len(minPathGrid)
	col := len(minPathGrid[0])
	minPath := 0

	if isValid(row, col, i + 1, j)&&isValid(row, col, i, j + 1) {
		minDown := minPathGrid[i + 1][j]
		minRight := minPathGrid[i][j + 1]
		if minDown < minRight {
			minPath = minDown
		} else {
			minPath = minRight
		}
	} else if isValid(row, col, i + 1, j) {
		minPath = minPathGrid[i + 1][j]
	} else if isValid(row, col, i, j + 1) {
		minPath = minPathGrid[i][j + 1]
	}

	return minPath
}

func isValid(row int, col int, i int, j int) bool {
	if 0 <= i&&i <= row - 1&&0 <= j&&j <= col - 1 {
		return true
	}
	return false
}