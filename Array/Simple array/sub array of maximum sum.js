function subArrayOfMaximumSum(arr) {
    if (!arr.length) {
        return []
    }

    let start = tempStart = end = 0
    let currMax = maxSum = arr[0]

    arr.forEach((number, i) => {

        if (number > (currMax+number)) {
            tempStart = i
            currMax = number
        } else {
            currMax += number
        }

        if (currMax > maxSum) {
            maxSum = currMax
            start = tempStart
            end = i
        }
    });

    return arr.slice(start,end+1)
}


console.log(subArrayOfMaximumSum([1,91,-300,-7, 4,2,9]))