package p242

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsAnagram(t *testing.T) {
	assert := require.New(t)
	assert.Equal(isAnagram("anagram", "nagaram"), true)
	assert.Equal(isAnagram("rat", "car"), false)
}
