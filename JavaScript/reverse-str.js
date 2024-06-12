function reverse_string(s) {
    let ar = s.split('')
    let result = [];
    ar?.map((s)=> {
        result.unshift(s)
    })
    return result.join("");  
}

// palindrome string
let str = 'harshit';
console.log("reverse_string: ", reverse_string(str))
