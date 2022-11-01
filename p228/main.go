package p228

import (
	"strconv"
)

type rang struct {
	low  int
	high int
}

func summaryRanges(nums []int) []string {
	ranges := make([]*rang, 0)
	for i := 0; i < len(nums); {
		low := i
		i++
		for ; i < len(nums) && nums[i-1]+1 == nums[i]; i++ {
		}
		ranges = append(ranges, &rang{nums[low], nums[i-1]})
	}
	results := make([]string, 0, len(ranges))
	for _, r := range ranges {
		if r.low == r.high {
			result := strconv.Itoa(r.low)
			results = append(results, result)
		} else {
			result := strconv.Itoa(r.low) + "->" + strconv.Itoa(r.high)
			results = append(results, result)
		}
	}
	return results
}
