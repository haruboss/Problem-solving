var getConcatenation = function(nums) {
    return [...nums, ...nums]
};

console(getConcatenation([1,2,1])) // [1,2,1,1,2,1]