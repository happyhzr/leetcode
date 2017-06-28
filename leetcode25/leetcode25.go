package leetcode25

import (
	"strconv"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) Len() int {
	len := 0
	for l != nil {
		l = l.Next
		len++
	}
	return len
}

type List struct {
	dummy *ListNode
	len   int
}

func (l *List) Len() int {
	return l.len
}

func (l *List) Head() *ListNode {
	return l.dummy.Next
}

func (l *List) String() string {
	str := ""
	curr := l.dummy.Next
	for curr != nil {
		str += strconv.Itoa(curr.Val)
		if curr.Next != nil {
			str += "->"
		}
		curr = curr.Next
	}
	return str
}

func (l *List) Insert(x int) {
	node := &ListNode{Val: x}
	node.Next = l.dummy.Next
	l.dummy.Next = node
	l.len++
}

func (l *List) ToSlice() []int {
	slice := make([]int, l.len)
	curr := l.dummy.Next
	for i := 0; i < l.len; i++ {
		slice[i] = curr.Val
		curr = curr.Next
	}
	return slice
}

func NewList() *List {
	return &List{dummy: &ListNode{}, len: 0}
}

func NewListFromSlice(slice []int) *List {
	list := NewList()
	for i := len(slice) - 1; i >= 0; i-- {
		list.Insert(slice[i])
	}
	return list
}

func NewListFromHead(head *ListNode) *List {
	dummy := &ListNode{Next: head}
	return &List{dummy: dummy, len: head.Len()}
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	curr := head
	count := 0
	for curr != nil && count < k {
		curr = curr.Next
		count++
	}
	if count < k {
		return head
	}

	tail := curr
	tail = reverseKGroup(tail, k)
	return reverseK(head, tail, k)
}

func reverseK(head *ListNode, tail *ListNode, k int) *ListNode {
	var tmp *ListNode
	for i := 0; i < k; i++ {
		tmp = head.Next
		head.Next = tail
		tail = head
		head = tmp
	}
	return tail
}
