package p228

import (
	"strconv"
)

type rang struct {
	low  int
	high int
}

func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return make([]string, 0)
	}
	ranges := make([]*rang, 0)
	low := 0
	high := 0
	for ; high < len(nums); high++ {
		if high > 0 && nums[high-1]+1 != nums[high] {
			ranges = append(ranges, &rang{nums[low], nums[high-1]})
			low = high
		}
	}
	ranges = append(ranges, &rang{nums[low], nums[high-1]})
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
