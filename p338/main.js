/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
    let counts = new Array(n + 1)
    for (let i = 0; i <= n; i++) {
        counts[i] = count(i)
    }
    return counts
};

function count(i) {
    let n = 0
    while (i !== 0) {
        i &= (i - 1)
        n++
    }
    return n
}

function main() {
    console.log(countBits(2))
    console.log(countBits(5))
}

main()