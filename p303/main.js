/**
 * @param {number[]} nums
 */
var NumArray = function (nums) {
    this.sums = new Array(nums.length + 1).fill(0)
    for (let i = 0; i < nums.length; i++) {
        this.sums[i + 1] = this.sums[i] + nums[i]
    }
    console.log(this.sums)
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function (left, right) {
    return this.sums[right + 1] - this.sums[left]
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */

function main() {
    const obj = new NumArray([-2, 0, 3, -5, 2, -1]);
    console.log(obj.sumRange(0, 2))
    console.log(obj.sumRange(2, 5))
    console.log(obj.sumRange(0, 5))
}

main()