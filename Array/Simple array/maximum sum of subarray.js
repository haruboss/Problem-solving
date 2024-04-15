function maximumSumSubArray(arr) {
    if (!arr.length) 
    return 0

    let maxSum = arr[0]
    let currMax = arr[0]

    arr.forEach(number => {
        currMax = Math.max(number, currMax + number)
        maxSum = Math.max(currMax, maxSum)
    });
    return maxSum
}

console.log(maximumSumSubArray([1,2,3,-6, 4,2,9]))