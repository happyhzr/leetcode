package main

import "fmt"

func main() {
	grid := [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	paths := uniquePathsWithObstacles(grid)
	fmt.Println(paths)
}

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) == 0 || len(obstacleGrid[0]) == 0 {
		return 0
	}

	row := len(obstacleGrid)
	col := len(obstacleGrid[0])

	pathGrid := initPathGrid(row, col)
	if obstacleGrid[row - 1][col - 1] == 0 {
		pathGrid[row - 1][col - 1] = 1
	} else {
		pathGrid[row - 1][col - 1] = 0
	}

	for i := row - 1; i >= 0; i-- {
		for j := col - 1; j >= 0; j-- {
			if i == row - 1&&j == col - 1 {
				continue
			}

			if obstacleGrid[i][j] == 0 {
				pathGrid[i][j] = getPaths(obstacleGrid, pathGrid, i + 1, j) + getPaths(obstacleGrid, pathGrid, i, j + 1)
			} else {
				pathGrid[i][j] = 0
			}
		}
	}
	//fmt.Println(pathGrid)

	return pathGrid[0][0]
}

func initPathGrid(row int, col int) [][]int {
	pathGrid := make([][]int, row)
	for i := 0; i < row; i++ {
		pathGrid[i] = make([]int, col)
	}
	return pathGrid
}

func getPaths(grid [][]int, pathGrid [][]int, i int, j int) int {
	row := len(grid)
	col := len(grid[0])

	if 0 <= i&&i <= row - 1&&0 <= j&&j <= col - 1&&grid[i][j] == 0 {
		return pathGrid[i][j]
	}
	return 0
}


