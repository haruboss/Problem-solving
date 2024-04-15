function buildArray(numbers) {
    const result = []
    numbers.forEach((_, i)=> {
        result.push(numbers[numbers[i]])
    })
    return result
    
};

console.log(buildArray([0,2,1,5,3,4])) // [0,1,2,4,5,3]

