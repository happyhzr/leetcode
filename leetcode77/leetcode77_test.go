package leetcode77

import (
	"testing"
	"sort"
)

type Test struct {
	input Input
	want  [][]int
}

type Input struct {
	n int
	k int
}

func TestCombine(t *testing.T) {
	tests := generateTests()

	for _, test := range tests {
		got := combine(test.input.n, test.input.k)
		if !slslequal(got, test.want) {
			t.Errorf("combine(%d, %d) = %v want: %v", test.input.n, test.input.k, got, test.want)
		}
	}
}

func generateTests() []Test {
	tests := []Test{
		{Input{4, 2}, [][]int{
			{2, 4},
			{3, 4},
			{2, 3},
			{1, 2},
			{1, 3},
			{1, 4},
		}},
	}
	return tests
}

func slslequal(slsl1 [][]int, slsl2 [][]int) bool {
	if len(slsl1) != len(slsl2) {
		return false
	}
	for _, sl1 := range slsl1 {
		if !slinslsl(sl1, slsl2) {
			return false
		}
	}
	for _, sl2 := range slsl2 {
		if !slinslsl(sl2, slsl1) {
			return false
		}
	}
	return true
}

func slinslsl(sl []int, slsl [][]int) bool {
	for _, sl2 := range slsl {
		if slequal(sl, sl2) {
			return true
		}
	}
	return false
}

func slequal(sl1 []int, sl2 []int) bool {
	if len(sl1) != len(sl2) {
		return false
	}
	dup1 := make([]int, len(sl1))
	dup2 := make([]int, len(sl2))
	copy(dup1, sl1)
	copy(dup2, sl2)
	sort.Ints(dup1)
	sort.Ints(dup2)
	for i := 0; i < len(dup1); i++ {
		if dup1[i] != dup2[i] {
			return false
		}
	}
	return true
}