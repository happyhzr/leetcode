package main

import "fmt"

func main() {
	ss := []string{
		"hello world",
		"hello",
		"      ",
		"hello   ",
		"    hello    ",
	}
	for _, v := range ss {
		fmt.Println(lengthOfLastWord(v))
	}
}

	func lengthOfLastWord(s string) int {
		last := len(s) - 1
		for ; last >= 0; last-- {
			if s[last] != ' ' {
				break
			}
		}

		lastWS := last
		for ; lastWS >= 0; lastWS-- {
			if s[lastWS] == ' ' {
				break
			}
		}

		return last - lastWS
	}
