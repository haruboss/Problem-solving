// https://leetcode.com/problems/find-pivot-index/
var pivotIndex = function(nums) {
    let totalSum = nums.reduce((sum, num) => sum + num, 0);
    let leftSum = 0
    for (let i=0;i<nums.length;i++) {
        rightSum = totalSum - nums[i] - leftSum
        if (leftSum === rightSum) return i

        leftSum += nums[i]
    }
    return -1
};

console.log(pivotIndex([1,7,3,6,5,6])) // 3