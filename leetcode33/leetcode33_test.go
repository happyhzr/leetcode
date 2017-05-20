package leetcode33

import (
	"fmt"
	"math/rand"
	"sort"
	"testing"

	"github.com/stretchr/testify/assert"
)

const (
	maxArraySize = 1024
	maxArrayNum  = 1024
	maxNum       = 1024 * 1024 * 1024
)

var (
	cache = map[int]struct{}{}
)

type testFindSmallestType struct {
	nums []int
	want int
}

func newNodupAsc(size int) ([]int, int) {
	nums := make([]int, 0, size)
	count := 0
	for count < size {
		num := rand.Intn(maxNum)
		_, ok := cache[num]
		if !ok {
			nums = append(nums, num)
			cache[num] = struct{}{}
			count++
		}
	}
	sort.Ints(nums)

	var rotate int
	if size > 0 {
		rotate = rand.Intn(size)
	}
	newNums := make([]int, size)
	copy(newNums, nums[rotate:])
	copy(newNums[size-rotate:], nums[:rotate])

	var index int
	if size == 0 {
		index = -1
	} else {
		index = size - rotate
		if index == size {
			index = 0
		}
	}

	return newNums, index
}

func newTestFindSmallestType() *testFindSmallestType {
	l := rand.Intn(maxArraySize + 1)

	nums, index := newNodupAsc(l)

	return &testFindSmallestType{
		nums: nums,
		want: index,
	}
}

func newTestFindSmallestTypes() []*testFindSmallestType {
	arrayNum := rand.Intn(maxArrayNum + 1)
	tests := make([]*testFindSmallestType, 0, arrayNum)
	for i := 0; i < arrayNum; i++ {
		tests = append(tests, newTestFindSmallestType())
	}
	return tests
}

func TestFindSmallest(t *testing.T) {
	assert := assert.New(t)

	tests := newTestFindSmallestTypes()
	for _, test := range tests {
		got := findSmallest(test.nums)
		assert.Equal(test.want, got, fmt.Sprint(test.nums))
	}
}

type testSearchType struct {
	nums   []int
	target int
	want   int
}

func newTestSearchType() *testSearchType {
	size := rand.Intn(maxArraySize + 1)
	nums, _ := newNodupAsc(size)
	want := rand.Intn(size)
	return &testSearchType{
		nums:   nums,
		target: nums[want],
		want:   want,
	}
}

func newTestSearchTypes() []*testSearchType {
	arrayNum := rand.Intn(maxArrayNum + 1)
	tests := make([]*testSearchType, 0, arrayNum)
	for i := 0; i < arrayNum; i++ {
		tests = append(tests, newTestSearchType())
	}
	return tests
}

func TestSearch(t *testing.T) {
	assert := assert.New(t)

	tests := newTestSearchTypes()
	for _, test := range tests {
		got := search(test.nums, test.target)
		assert.Equal(test.want, got, fmt.Sprint(test.nums, test.target))
	}
}
