// #1
function reverse(arr) {
    for ( x = 0; x < arr.length / 2; x++) {
        holder = arr[x]
        arr[x] = arr[arr.length - 1 - x]
        arr[arr.length - 1 - x] = holder
    }
    return (arr)
}
console.log(reverse([15,2,4,3,5,6,75,8,9,32]))

// #2
function rotateArr(arr, shiftBy) {
    if (shiftBy < 0) {
        var offset = shiftBy * -1
    } else {
        var offset = shiftBy
    }
    while (offset > 0 ) {
        if (shiftBy < 0) {
            var holder = arr[0]
            for (var x = 0; x  < arr.length; x++) {
                arr[x] = arr[x + 1]
            }
            arr[arr.length - 1] = holder
        } else {
            var holder = arr[arr.length - 1]
            for (var x = arr.length - 1; x > 0; x--) {
                arr[x] = arr[x - 1]
            }
            arr[0] =  holder
        }
        offset--
    }
    return arr
}
console.log(rotateArr([1,2,3,4,5], -2))

// #3
function filterRange(arr, min, max) {
    var holder = 0
    for ( var x = 0; x < arr.length; x++) {
        if ((arr[x] >= min) && (arr[x] <= max)) {
            arr[holder] = arr[x]
            holder++
        }
    }
    arr.length = holder
    return arr
}
console.log(filterRange([15,2,4,3,5,6,75,8,9,32], 8, 35))

// #4
function arrConcat(arr1, arr2) {
    var holder = 0
    arr = []
    for ( var x = 0; x < arr1.length; x++) {
        arr[holder] = arr1[x]
        holder++
    }
    for ( var x = 0; x < arr2.length; x++) {
        arr[holder] = arr2[x]
        holder++
    }
    return arr
}
console.log(arrConcat([15,2,4,3,5,6,75,8,9,32], [8, 35,'trd','sdfdsfwe','32', 78]))