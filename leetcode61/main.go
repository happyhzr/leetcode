package main

import "fmt"

func main() {
	sl := []int{1}
	k := 1
	reverse(sl)
	dummy := New(sl)
	list := rotateRight(dummy.Next, k)
	newSlice := convert(list)
	fmt.Println(newSlice)
}

func reverse(sl []int) {
	i, j := 0, len(sl) - 1
	for i < j {
		sl[i], sl[j] = sl[j], sl[i]
		i++
		j--
	}
}

func convert(head *ListNode) []int {
	sl := make([]int, 0)
	for head != nil {
		sl = append(sl, head.Val)
		head = head.Next
	}
	return sl
}

//Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func New(sl []int) *ListNode {
	dummy := &ListNode{0, nil}
	for _, v := range sl {
		dummy.add(v)
	}
	return dummy
}

func (dummy *ListNode)add(value int) {
	node := &ListNode{value, nil}
	node.Next = dummy.Next
	dummy.Next = node
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}

	var headr, tailr, headl, taill *ListNode
	headr = head
	size := 0
	for headr != nil {
		headr = headr.Next
		size++
	}
	if size == 0 {
		return head
	}

	k %= size
	if k == 0 {
		return head
	}
	k = size - k
	headr = head
	for i := 0; i < k; i++ {
		headr = headr.Next
	}
	tailr = headr
	for tailr.Next != nil {
		tailr = tailr.Next
	}
	headl = head
	taill = head
	for i := 0; i < k - 1; i++ {
		taill = taill.Next
	}
	tailr.Next = headl
	taill.Next = nil
	return headr
}
