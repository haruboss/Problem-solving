function find_kth_largest_smallest_num(numbers, k) {
    if (numbers?.length < 2) {
        return numbers
    }

    // implemented bubble sort 
    for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < numbers.length - i - 1; j++) {
            if (numbers[j] > numbers[j + 1]) {
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            }
        }
    }
// 2nd largest number 
    const max = numbers[numbers.length - k];
    const min = numbers[k - 1];
    
    return {min, max}
}


console.log(find_kth_largest_smallest_num([3,2, 31, 10, 32, 100], 2))