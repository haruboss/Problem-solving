// Find a peak element which is not smaller than its neighbours
// Input: array[]= {5, 10, 20, 15}
// Output: 20

// Input: array[] = {10, 20, 15, 2, 23, 90, 67}
// Output: 20 or 90

function findPeakElement(arr) {
    if (!arr.length) {
        return []
    }
    const peakEl =[]
    for (let i = 1; i < arr.length - 1; i++) {
        if (arr[i-1] < arr[i] && arr[i] > arr[i+1]) {
            peakEl.push(arr[i])
        }
    }
    return peakEl
}

console.log(findPeakElement([10, 20, 15, 2, 23, 90, 67, 68, 34]))
