package p39

import (
	"slices"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCombinationSum(t *testing.T) {
	assert := assert.New(t)

	candidates := []int{2, 3, 6, 7}
	target := 7
	expected := [][]int{{2, 2, 3}, {7}}
	actual := combinationSum(candidates, target)
	assert.True(equal(expected, actual))

	candidates = []int{2, 3, 5}
	target = 8
	expected = [][]int{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}}
	actual = combinationSum(candidates, target)

	assert.True(equal(expected, actual))

	candidates = []int{2}
	target = 1
	expected = [][]int{}
	actual = combinationSum(candidates, target)
	assert.True(equal(expected, actual))
}

func equal(a [][]int, b [][]int) bool {
	for _, aSlice := range a {
		if !in(aSlice, b) {
			return false
		}
	}
	for _, bSlice := range b {
		if !in(bSlice, a) {
			return false
		}
	}
	return true
}

func in(a []int, as [][]int) bool {
	for _, arr := range as {
		if slices.Equal(a, arr) {
			return true
		}
	}
	return false
}
