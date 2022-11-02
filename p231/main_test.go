package p231

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsPowerOfTwo(t *testing.T) {
	assert := require.New(t)
	assert.Equal(true, isPowerOfTwo(1))
	assert.Equal(true, isPowerOfTwo(16))
	assert.Equal(false, isPowerOfTwo(3))
	assert.Equal(true, isPowerOfTwo(4))
	assert.Equal(false, isPowerOfTwo(5))
	assert.Equal(false, isPowerOfTwo(-1))
}
