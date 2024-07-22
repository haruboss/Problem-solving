// Input: [2,3,54,6,4]
// output: [4,6,54,3,2]

function reverseArray(arr) {
    if (arr.length < 2 ) return arr
    const resultArr = []

    for(let i = arr.length - 1; i >= 0; i--) {
        resultArr.push(arr[i])
    }
    return resultArr
}

function reverseArrayTwoPointer(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        // Swap the elements
        [arr[left], arr[right]] = [arr[right], arr[left]];

        // Move the pointers
        left++;
        right--;
    }

    return arr;
}

// Example usage:
let array = [1, 2, 3, 4, 5, 8];
console.log(reverseArrayTwoPointer(array)); // Output: [5, 4, 3, 2, 1]


// console.log(reverseArray([2,3,54,6,4]))