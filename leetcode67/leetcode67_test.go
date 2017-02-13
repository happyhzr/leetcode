package leetcode67

import "testing"

func TestAddBinary(t *testing.T) {
	tests := []struct {
		a    string
		b    string
		want string
	}{
		{"0", "1", "1"},
		{"1", "1", "10"},
		{"111111", "1", "1000000"},
		{"111111", "11", "1000010"},
		{"100", "110010", "110110"},
	}

	format := "addBinary(%q, %q) = %q"
	for _, test := range tests {
		got := AddBinary(test.a, test.b)
		if got != test.want {
			t.Errorf(format, test.a, test.b, got)
		}
	}
}
