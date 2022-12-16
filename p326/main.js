/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
    if (n <= 0) {
        return false
    }
    return 1162261467 % n === 0
};

function main() {
    console.log(isPowerOfThree(27))
    console.log(isPowerOfThree(0))
    console.log(isPowerOfThree(9))
    console.log(isPowerOfThree(45))
}

main()