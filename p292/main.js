/**
 * @param {number} n
 * @return {boolean}
 */
var canWinNim = function (n) {
    return n % 4 !== 0
};

function main() {
    console.log(canWinNim(4))
    console.log(canWinNim(1))
    console.log(canWinNim(2))
}

main()