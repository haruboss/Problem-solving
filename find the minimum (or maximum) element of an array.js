// Given an array, write functions to find the minimum and maximum elements in it. 
// input: [2,3,54,6,4]
// outtput: min: 2, max: 54

function findMinMax(arr) {
    if (!arr.length) {
        return null
    }
    let min = Infinity;
    let max = -Infinity
    arr.forEach(number => {
        if(number > max) {
            max = number
        }
        if(number < min) {
            min = number
        }
    });
    return {min, max}
}

console.log(findMinMax([2,3,-1, 54,65, 6,4]))