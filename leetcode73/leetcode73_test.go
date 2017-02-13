package leetcode73

import "testing"

type matrix [][]int

func TestSetZeroes(t *testing.T) {
	tests := []struct {
		input matrix
		want  matrix
	}{
		{matrix{{}}, matrix{{}}},
		{matrix{{1}}, matrix{{1}}},
		{matrix{{0}}, matrix{{0}}},
		{matrix{{0, 1}, {1, 1}}, matrix{{0, 0}, {0, 1}}},
		{matrix{{0, 0}, {1, 1}}, matrix{{0, 0}, {0, 0}}},
		{matrix{{0, 1}, {0, 1}}, matrix{{0, 0}, {0, 0}}},
		{matrix{{0, 0}, {0, 1}}, matrix{{0, 0}, {0, 0}}},
		{matrix{{0, 0}, {0, 0}}, matrix{{0, 0}, {0, 0}}},
	}

	format := "setZeroes(%v) = %v"
	for _, test := range tests {
		cop := copyMatrix(test.input)
		setZeroes(cop)
		if !isEqualMatrix(cop, test.want) {
			t.Errorf(format, test.input, cop)
		}
	}
}

func isEqualMatrix(m1 matrix, m2 matrix) bool {
	if len(m1) != len(m2) {
		return false
	}

	for i := 0; i < len(m1); i++ {
		if !isEqualRow(m1[i], m2[i]) {
			return false
		}
	}

	return true
}

func isEqualRow(row1 []int, row2 []int) bool {
	if len(row1) != len(row2) {
		return false
	}

	for j := 0; j < len(row1); j++ {
		if row1[j] != row2[j] {
			return false
		}
	}

	return true
}
