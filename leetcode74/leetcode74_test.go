package leetcode74

import "testing"

type Matrix [][]int
type inputType struct {
	matrix Matrix
	target int
}

func TestSearchMatrix(t *testing.T) {
	tests := []struct {
		input inputType
		want  bool
	}{
		{inputType{Matrix{}, 0}, false},
		{inputType{Matrix{{}}, 0}, false},
		{inputType{Matrix{
			{1, 3, 5, 7},
			{10, 11, 16, 20},
			{23, 30, 34, 50},
		}, 3}, true},
		{inputType{Matrix{
			{1, 1},
		}, 2}, false},
	}

	for _, test := range tests {
		got := searchMatrix(test.input.matrix, test.input.target)
		{
			if got != test.want {
				t.Errorf("searchMatrix(%v) = %b", test.input.matrix, test.want)
			}
		}
	}
}
