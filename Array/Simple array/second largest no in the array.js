function secondLargestNumber(arr) {
    if (arr.length < 2) {
        return null
    }
    let firstMax = SecondMax = 0
    arr.forEach(num => {
        if (num > firstMax) {
            SecondMax = firstMax
            firstMax = num
        } else if (num > SecondMax && (num !== firstMax)) {
            SecondMax = num
        }
    });

    return SecondMax
}


console.log(secondLargestNumber([1,2,4,5,6,6]))