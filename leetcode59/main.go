package main

import "fmt"

func main() {
	n := 3
	matrix := generateMatrix(n)
	for _, v := range matrix {
		for _, u := range v {
			fmt.Print(u, " ")
		}
		fmt.Println()
	}
}

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, n)
	}

	loop := n / 2
	i, j := 0, 0
	a := 1
	for k := 0; k < loop; k++ {
		for ; j < n - 1 - k; j++ {
			matrix[i][j] = a
			a++
		}
		for ; i < n - 1 - k; i++ {
			matrix[i][j] = a
			a++
		}
		for ; j >= 1 + k; j-- {
			matrix[i][j] = a
			a++
		}
		for ; i >= 1 + k; i-- {
			matrix[i][j] = a
			a++
		}
		i++
		j++
	}
	if n % 2 == 1 {
		matrix[loop][loop] = a
	}
	return matrix
}
