package p38

import (
	"errors"
	"strconv"
	"strings"
)

func countAndSay(n int) string {
	a := make([]string, n+1)
	a[1] = "1"
	for i := 2; i <= n; i++ {
		a[i], _ = count(a[i-1])
	}
	return a[n]
}

func count(s string) (string, error) {
	if len(s) == 0 {
		return "", errors.New("string is empty")
	}
	prev := ' '
	n := 0
	output := &strings.Builder{}
	for i, c := range s {
		if i == 0 {
			prev = c
		}
		if prev == c {
			n++
		} else {
			output.WriteString(strconv.Itoa(n))
			output.WriteRune(prev)
			prev = c
			n = 1
		}
	}
	output.WriteString(strconv.Itoa(n))
	output.WriteRune(prev)
	return output.String(), nil
}
