function debounce(func, delay) {
    let timestamp;

    return (...arg) => {
        clearInterval(timestamp)
        timestamp = setTimeout(() => {
            func(...arg)
        }, delay);
    }
}

function search(query) {
    return "result: ", query;
}

const debounceSearch = debounce(search, '3000')

const input = document.querySelector("Input.query");
input.addEventListener('input', (event)=> {
    const query = event.target.query;
    debounceSearch(query)
})