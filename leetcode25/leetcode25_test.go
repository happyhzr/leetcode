package leetcode25

import (
	"math/rand"
	"testing"

	"time"

	"github.com/stretchr/testify/require"
)

const (
	maxNumPerSlice = 1024
	sliceNum       = 1024
)

type reverseKGroupStruct struct {
	slice []int
	k     int
}

func TestReverseKGroup(t *testing.T) {
	assert := require.New(t)
	seed := time.Now().Unix()
	t.Logf("seed: %d\n", seed)
	tests := genTests(seed)

	for _, test := range tests {
		list := NewListFromSlice(test.slice)
		head := list.Head()
		head = reverseKGroup(head, test.k)
		list = NewListFromHead(head)
		got := list.ToSlice()
		want := test.slice
		reverseKGroupSlice(want, test.k)
		assert.Equal(want, got)
	}
}

func reverseKSlice(slice []int, k int) {
	if len(slice) < k {
		return
	}
	low, high := 0, k-1
	for low < high {
		slice[low], slice[high] = slice[high], slice[low]
		low++
		high--
	}
}

func reverseKGroupSlice(slice []int, k int) {
	for i := 0; i < len(slice); i += k {
		tail := i + k
		if tail > len(slice) {
			tail = len(slice)
		}
		reverseKSlice(slice[i:tail], k)
	}
}

func genTest(seed int64) *reverseKGroupStruct {
	r := rand.New(rand.NewSource(seed))
	len := r.Intn(maxNumPerSlice)
	slice := make([]int, len)
	for i := 0; i < len; i++ {
		slice[i] = r.Int()
	}
	k := r.Intn(len) + 1
	return &reverseKGroupStruct{slice: slice, k: k}
}

func genTests(seed int64) []*reverseKGroupStruct {
	tests := make([]*reverseKGroupStruct, 0, sliceNum)
	for i := 0; i < sliceNum; i++ {
		tests = append(tests, genTest(seed))
	}
	return tests
}
