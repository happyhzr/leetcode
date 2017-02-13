package leetcode71

import "testing"

func TestSimplifyPath(t *testing.T) {
	tests := []struct {
		input string
		want  string
	}{
		{"/home/", "/home"},
		{"///home/", "/home"},
		{"/a/./b/../../c/", "/c"},
		{"/a/../../b/../../../c", "/c"},
	}

	format := "simplifyPath(%q) = %q\n"
	for _, test := range tests {
		got := simplifyPath(test.input)
		if got != test.want {
			t.Errorf(format, test.input, got)
		}
	}
}
