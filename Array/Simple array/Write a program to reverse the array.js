// Input: [2,3,54,6,4]
// output: [4,6,54,3,2]

function reverseArray(arr) {
    if (arr.length < 2 ) return arr
    const resultArr = []

    for(let i=arr.length-1; i>=0; i--) {
        resultArr.push(arr[i])
    }
    return resultArr
}

console.log(reverseArray([2,3,54,6,4]))