package main

import "fmt"

func main() {
	n, k := 3, 5
	permuation := getPermutation(n, k)
	fmt.Println(permuation)
}

func getPermutation(n int, k int) string {
	k--
	permutation := make([]byte, n)
	list := New()
	for i := n; i >= 1; i-- {
		list.Insert(i)
	}
	segnum := 1
	for i := 2; i <= n; i++ {
		segnum *= i
	}

	for i := 0; i < n; i++ {
		segnum /= (n - i)
		seg := k / segnum
		k %= segnum

		permutation[i] = byte(list.get(seg) + '0')
		list.remove(seg)
	}
	return string(permutation)
}

type List struct {
	Head *ListNode
}

func New() List {
	head := &ListNode{0, nil}
	return List{head}
}

func (this List) Insert(e int) {
	node := &ListNode{e, nil}
	node.Next = this.Head.Next
	this.Head.Next = node
}

func (this List)get(index int) int {
	node := this.Head.Next
	for i := 0; i < index; i++ {
		node = node.Next
	}
	return node.E
}

func (this List)remove(index int) {
	node := this.Head
	for i := 0; i < index; i++ {
		node = node.Next
	}
	node.Next = node.Next.Next
}

type ListNode struct {
	E    int
	Next *ListNode
}

