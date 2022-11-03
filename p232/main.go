package p232

type MyQueue struct {
	in  []int
	out []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) Push(x int) {
	this.in = append(this.in, x)
}

func (this *MyQueue) Pop() int {
	if len(this.out) == 0 {
		this.in2out()
	}
	v := this.out[len(this.out)-1]
	this.out = this.out[:len(this.out)-1]
	return v
}

func (this *MyQueue) Peek() int {
	if len(this.out) == 0 {
		this.in2out()
	}
	return this.out[len(this.out)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.in) == 0 && len(this.out) == 0
}

func (q *MyQueue) in2out() {
	for len(q.in) > 0 {
		v := q.in[len(q.in)-1]
		q.out = append(q.out, v)
		q.in = q.in[:len(q.in)-1]
	}
}
