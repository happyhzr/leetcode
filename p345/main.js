/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
    const a = Array.from(s)
    const n = s.length
    let i = 0
    let j = n - 1
    while (i < j) {
        while (i < n && !isVowel(a[i])) {
            i++
        }
        while (j >= 0 && !isVowel(a[j])) {
            j--
        }
        if (i < j) {
            [a[i], a[j]] = [a[j], a[i]]
            i++
            j--
        }
    }
    return a.join("")
};

function isVowel(c) {
    return "aeiouAEIOU".indexOf(c) !== -1
}

function main() {
    console.log(reverseVowels("hello"))
    console.log(reverseVowels("leetcode"))
}

main()