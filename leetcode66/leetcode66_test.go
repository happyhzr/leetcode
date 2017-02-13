package leetcode66

import "testing"

type test struct {
	input []int
	want  []int
}

func TestPlusOne(t *testing.T) {
	tests := []test{
		{[]int{0}, []int{1}},
		{[]int{8}, []int{9}},
		{[]int{9}, []int{1, 0}},
		{[]int{9, 9}, []int{1, 0, 0}},
	}

	format := "plusOne(%v) = %v"
	for _, test := range tests {
		got := plusOne(test.input)
		if !isEqualSlice(got, test.want) {
			t.Errorf(format, test.input, got)
		}
	}
}

func isEqualSlice(sl1 []int, sl2 []int) bool {
	len1 := len(sl1)
	len2 := len(sl2)
	if len1 != len2 {
		return false
	}

	for i := 0; i < len1; i++ {
		if sl1[i] != sl2[i] {
			return false
		}
	}
	return true
}
