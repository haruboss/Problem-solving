function secondLargestNumber(arr) {
    if (arr.length < 2) {
        return -1
    }
    let firstMax = secondMax = 0
    arr.forEach(num => {
        if (num > firstMax) {
            secondMax = firstMax
            firstMax = num
        } else if (num > secondMax && (num !== firstMax)) {
            secondMax = num
        }
    });

    return secondMax
}


console.log(secondLargestNumber([1,2,4,5,6,6]))