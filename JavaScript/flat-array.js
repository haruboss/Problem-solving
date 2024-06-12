function toFlat(array) {
    const result = array.reduce((flat, toFlattern) => {
        return flat.concat(Array.isArray(toFlattern) ? toFlat(toFlattern) : toFlattern);
    }, []);
    return result;
}

arr = [1,2,[4,[5, 6], 8], 9]
flat_arr = toFlat(arr)
console.log(flat_arr)