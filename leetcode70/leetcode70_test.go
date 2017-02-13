package leetcode70

import "testing"

func TestClimbStairs(t *testing.T) {
	tests := []struct {
		input int
		want  int
	}{
		{1, 1},
		{2, 2},
		{3, 3},
	}

	format := "climbStairs(%d) = %d\n"
	for _, test := range tests {
		got := climbStairs(test.input)
		if got != test.want {
			t.Errorf(format, test.input, got)
		}
	}
}
