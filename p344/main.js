/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
    const n = s.length
    for (let i = 0, j = n - 1; i < j; i++, j--) {
        [s[i], s[j]] = [s[j], s[i]]
    }
};

function main() {
    let a = ["h", "e", "l", "l", "o"]
    reverseString(a)
    console.log(a)
    a = ["H", "a", "n", "n", "a", "h"]
    reverseString(a)
    console.log(a)
}

main()