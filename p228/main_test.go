package p228

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestSummaryRanges(t *testing.T) {
	assert := require.New(t)
	assert.Equal([]string{"0->2", "4->5", "7"}, summaryRanges([]int{0, 1, 2, 4, 5, 7}))
	assert.Equal([]string{"0", "2->4", "6", "8->9"}, summaryRanges([]int{0, 2, 3, 4, 6, 8, 9}))
	assert.Equal([]string{}, summaryRanges([]int{}))
	assert.Equal([]string{"0"}, summaryRanges([]int{0}))
	assert.Equal([]string{"0->1"}, summaryRanges([]int{0, 1}))
}
