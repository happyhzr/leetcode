/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
    return n > 0 && (n & (n - 1)) === 0 && (n & 0xaaaaaaaa) === 0
};

function main() {
    console.log(isPowerOfFour(16))
    console.log(isPowerOfFour(5))
    console.log(isPowerOfFour(1))
}

main()