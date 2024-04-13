function thirdLargestNum(arr) {
    if (arr.length < 3) {
        return null
    }
    let firstMax = secondMax = thirdMax = -Infinity;
    arr.forEach(num => {
        if (num > firstMax) {
            thirdMax = secondMax
            secondMax = firstMax
            firstMax = num
        } else if (num > secondMax && num != firstMax) {
            thirdMax = secondMax
            secondMax = num
        } else if (num > thirdMax && num != firstMax && num !== secondMax) {
            thirdMax = num
        }
    });


    return thirdMax !== -Infinity ? thirdMax : null; 
}

console.log(thirdLargestNum([2,3, 40,10,6]))