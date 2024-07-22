const customMap = function(cb) {
    const res = [];
    for (let i = 0; i < this.length; i++) {
       res.push(cb(this[i], i))
    }
	return res
}

const customFilter = function(cb) {
    const res= [];
    for(let i = 0; i < this.length; i++) {
        if (cb(this[i], i)) {
            res.push(this[i])
        }
    }
	return res
}

const customForEach = function(cb) {
    for(let i = 0; i < this.length; i++) {
        cb(this[i], i)
    }
}

const customReduce = function( cb,acc) {
    for(let i = 0; i < this.length; i++) {
       acc = cb(acc,this[i])
    }
    return acc;
}

Array.prototype.myMap = customMap

Array.prototype.myFilter = customFilter

Array.prototype.myForEach = customForEach

Array.prototype.myReduce = customReduce

// const r = [1,2,3,5].myMap((n) => n*2)
const r = [1,2,3,5]
let a = r.myForEach((n) => n*2)
console.log(r)
console.log(a)