// https://leetcode.com/problems/find-the-highest-altitude/

// Input: gain = [-5,1,5,0,-7]
// Output: 1
// Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

var largestAltitude = function(gain) {
    const result = [0]
    let highestAltitude = 0
    for (let i=0;i<gain.length;i++) {
        const altitude = result[i]+gain[i]
        if (altitude > highestAltitude) {
            highestAltitude = altitude
        }
        result.push(altitude)
    }
    return highestAltitude
};

console.log(largestAltitude([-5,1,5,0,-7])) // 1