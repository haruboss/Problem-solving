function catching() {
    const catchingObj = {}
    
    return (key) => {
        if (key in catchingObj) {
            return catchingObj[key]
        }

        let newObj = {
            key: key
        }
        catchingObj[key] = newObj
        return newObj;
    }
}