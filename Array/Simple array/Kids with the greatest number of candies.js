// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
var kidsWithCandies = function(candies, extraCandies) {
    if (!candies.length || !extraCandies) {
        return null
    }
    const maxCandies = Math.max(...candies)
    return candies.map((candie) => maxCandies <= (extraCandies + candie))
};

const candies = [2,3,5,1,3]
const extraCandies = 3

console.log(kidsWithCandies(candies, extraCandies)) // output: [true,true,true,false,true]