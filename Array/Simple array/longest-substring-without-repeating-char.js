// function loangest_substring_without_repeating_char(s) {
//     if (s.length < 2) return s

//     let start = 0, end = 0, maxLength = 0

//     visited = new Set()
    
//     while (end < s.length) {
//         if (!visited.has(s[end])) {
//             visited.add(s[end])
//             end++
//             maxLength = Math.max(maxLength, visited.size)
//         } else {
//             visited.delete(s[start])
//             start++
//         }

//     }
//     return {maxLength, start, end}

// }

// s= 'aasds'
// result = loangest_substring_without_repeating_char(s)

// console.log(result)


function getUniqueCharacterSubstring(input) {
    const visited = new Map();
    let maxLength = 0;
    let start = 0;
    let output = "";

    for (let end = 0; end < input.length; end++) {
        const currChar = input[end];

        // If currChar is already in the map, move the start right after the last occurrence
        if (visited.has(currChar)) {
            start = Math.max(visited.get(currChar) + 1, start);
        }

        // Update the map with the current index of currChar
        visited.set(currChar, end);

        // Check if the current window length is the longest so far
        if (end - start + 1 > maxLength) {
            maxLength = end - start + 1;
            output = input.substring(start, end + 1);
        }
    }

    return output;
}

// Example usage:
console.log(getUniqueCharacterSubstring("abcabcbb")); // Output: "abc"
console.log(getUniqueCharacterSubstring("bbbbb"));    // Output: "b"
console.log(getUniqueCharacterSubstring("pwwkew"));   // Output: "wke"
console.log(getUniqueCharacterSubstring(""));         // Output: ""
