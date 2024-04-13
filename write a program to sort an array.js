// Input: [2,4,1,6,3]
// Output: [1,2,3,4,6]


function bblSort(arr) {
    if (arr.length < 2) {
        return arr
    }
    for (let i=0; i<=arr.length;i++) {
        for (let j=0; j<=arr.length-i-1;j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
    return arr
}

// not tested 
function selectionSort(arr) {
    if (arr.length < 2) {
        return arr
    }
    for (let i=0; i<=arr.length; i++) {
        for (let j=i; j<arr.length; j++) {
            if (arr[j] < arr[j+1]) {
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            }
        }
    }
    return arr
}

console.log(selectionSort([2,4,1,6,3]))