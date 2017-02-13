package leetcode67

func AddBinary(a string, b string) string {
	s := make([]byte, 0)
	i := len(a) - 1
	j := len(b) - 1

	var carry byte = 0
	for i >= 0 || j >= 0 || carry == 1 {
		if i >= 0 {
			carry += a[i] - '0'
			i--
		}
		if j >= 0 {
			carry += b[j] - '0'
			j--
		}
		p := []byte{carry % 2 + '0'}
		s = append(p, s...)
		carry /= 2
	}
	return string(s)
}