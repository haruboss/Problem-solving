// arr = [1,2,3]
// output: [6, 3, 2]

function productArrayExpectSelf(arr) {
    const n = arr.length

    const result = []
    let leftProduct = 1
    for (let i=0;i<n;i++) {
        result[i] = leftProduct
        leftProduct *= arr[i]
    }

    let rightProduct = 1
    for (let i=n-1;i>=0;i--) {
        result[i] *= rightProduct
        rightProduct *= arr[i]
    }

    return result
}

console.log(productArrayExpectSelf([1,2,3,4]))



