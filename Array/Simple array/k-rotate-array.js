k=2
arr=[1,2,3,4,5]
output: arr=[4,5,1,2,3] 

function rotateArray(arr, k) {
    if (!arr.length) {
        return arr
    }
    if (k > arr.length) {
        k = k % arr.length
    }
    const extractedElements = arr.splice(arr.length - k);

    // Add the extracted elements to the beginning of the array
    arr.unshift(...extractedElements);
    return arr
}


console.log(rotateArray([1,2,3,4,5], 8))