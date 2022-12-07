/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    let want = (0 + nums.length) * (nums.length + 1) / 2
    let got = 0
    nums.forEach(num => got += num)
    return want - got
};

function main() {
    console.log(missingNumber([3, 0, 1]))
    console.log(missingNumber([0, 1]))
    console.log(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    console.log(missingNumber([0]))
}

main()