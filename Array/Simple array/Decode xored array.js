// https://leetcode.com/problems/decode-xored-array/
var decode = function(encoded, first) {
    result = [first]
    let encNum = first
    encoded.map((num)=> {
        encNum = num^encNum
        result.push(encNum)
    })
    return result
};

console.log(decode([1,2,3], 1)) // [1,0,2,1]

// console.log(decode([6,2,7,3]), 4) // [4,2,0,7,4]