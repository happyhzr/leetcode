package leetcode71

import "strings"

func simplifyPath(path string) string {
	paths := strings.Split(path, "/")
	newPaths := make([]string, 0)

	for i := 0; i < len(paths); i++ {
		path = paths[i]
		if path == "" || path == "." {
			continue
		}
		if path == ".." {
			if len(newPaths) > 0 {
				newPaths = newPaths[:len(newPaths) - 1]
			}
			continue
		}
		newPaths = append(newPaths, path)
	}

	if len(newPaths) == 0 {
		return "/"
	}
	newPath := ""
	for i := 0; i < len(newPaths); i++ {
		newPath += "/" + newPaths[i]
	}

	return newPath
}
