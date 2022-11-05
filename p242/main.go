package p242

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	m1 := make(map[rune]int)
	m2 := make(map[rune]int)
	for _, c := range s {
		m1[c]++
	}
	for _, c := range t {
		m2[c]++
	}
	if len(m1) != len(m2) {
		return false
	}
	for k, v := range m1 {
		if v != m2[k] {
			return false
		}
	}
	return true
}
