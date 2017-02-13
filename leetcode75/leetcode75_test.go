package leetcode75

import (
	"testing"
	"math/rand"
	"sort"
)

type Test struct {
	input []int
	want  []int
}

func TestSortColors(t *testing.T) {
	tests := generateTests(1000, 1000)

	for _, test := range tests {
		dup := make([]int, len(test.input))
		copy(dup, test.input)
		sortColors(test.input)
		if !isEqualSlice(test.input, test.want) {
			t.Errorf("sortColors(%v) = %v want: %v", dup, test.input, test.want)
		}
	}
}

func generateTests(MAXM, MAXN int) []Test {
	tests := make([]Test, MAXN)
	for i := 0; i < MAXM; i++ {
		tests[i] = generateTest(MAXN)
	}

	return tests
}

func generateTest(maxLen int) Test {
	MAX := 2 //[0,MAX-1]
	length := rand.Intn(maxLen)
	var test Test
	test.input = make([]int, length)
	for i := 0; i < length; i++ {
		test.input[i] = rand.Intn(MAX)
	}

	test.want = make([]int, length)
	copy(test.want, test.input)
	sort.Ints(test.want)

	return test
}

func isEqualSlice(sl1 []int, sl2 []int) bool {
	if len(sl1) != len(sl2) {
		return false
	}
	for i := 0; i < len(sl1); i++ {
		if sl1[i] != sl2[i] {
			return false
		}
	}
	return true
}
