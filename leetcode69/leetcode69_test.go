package leetcode69

import "testing"

func TestMySqrt(t *testing.T) {
	tests := []struct {
		input int
		want  int
	}{
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 1},
		{4, 2},
		{5, 2},
		{6, 2},
		{7, 2},
		{8, 2},
		{9, 3},
		{10, 3},
	}

	format := "mySqrt(%d) = %d\n"
	for _, test := range tests {
		got := mySqrt(test.input)
		if got != test.want {
			t.Errorf(format, test.input, got)
		}
	}
}
