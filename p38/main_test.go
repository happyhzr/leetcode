package p38

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountAndSay(t *testing.T) {
	assert := assert.New(t)
	in := 1
	out := countAndSay(in)
	assert.Equal("1", out)
	in = 4
	out = countAndSay(in)
	assert.Equal("1211", out)
}

func TestCount(t *testing.T) {
	assert := assert.New(t)
	input := "3322251"
	output, err := count(input)
	assert.Nil(err)
	assert.Equal("23321511", output)
}
