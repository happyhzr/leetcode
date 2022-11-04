package p234

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	values := make([]int, 0)
	for ; head != nil; head = head.Next {
		values = append(values, head.Val)
	}
	for i, j := 0, len(values)-1; i < j; {
		if values[i] != values[j] {
			return false
		}
		i++
		j--
	}
	return true
}
