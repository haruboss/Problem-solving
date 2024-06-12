function count_of_number(arr) {
    return arr.reduce((acc, value) => {
        if (acc[value]) {
        acc[value] += 1
        } else {
            acc[value] = 1;
        }
        return acc;

    }, {});
}

arr = [1,2,3,3,4, 2]
counts_arr = count_of_number(arr)
console.log(counts_arr)