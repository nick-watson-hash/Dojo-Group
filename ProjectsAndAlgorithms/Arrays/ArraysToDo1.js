// #1
function pushFront(arr, num) {
    for ( var x = 0; x < arr.length; x++) {
    }
    arr[0] = num
    return (arr)
}
console.log(pushFront([20,-3,100,21,0,1,-24,-12], 25))

// #2
function popFront(arr) {
    for ( var x = 0; x < arr.length; x++) {
    }
    first = arr[0]
    arr.splice(0, 1)
    return (first)
}
console.log(popFront([20,-3,100,21,0,1,-24,-12]))

// #3
function insertAt(arr, val) {
    for ( var x = 0; x < arr.length; x++) {
    }
    arr[0] = val
    return (arr)
}
console.log(insertAt([20,-3,100,21,0,1,-24,-12], 25))

// #4
function removeAt(arr) {
    for ( var x = 0; x < arr.length; x++) {
    }
    arr.splice(0, 1)
    return (arr[0])
}
console.log(removeAt([20,-3,100,21,0,1,-24,-12], 25))

// #5
function removeAt(arr) {
    for ( var x = 0; x < arr.length; x++) {
        console.log(arr[arr.length -1])
        if (arr.length % 2 == 1) {
            arr[arr.length -1] = arr[arr.length -1]
        }
    }
    return (arr)
}
console.log(removeAt([1,2,3,4,5]))