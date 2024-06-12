function reverse_arr(arr) {
    let start = 0
    let end = arr.length - 1

    while (start < end) {
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start++
        end--
    }
    return arr
}

revered_arr = reverse_arr([1,2,3,6,4])
console.log(revered_arr)