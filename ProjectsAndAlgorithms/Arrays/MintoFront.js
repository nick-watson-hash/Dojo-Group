function minToFront(arr) {
    temp = arr[0]
    for ( x = 0; x < arr.length; x++) {
        if (arr[x] < temp) {
            temp = arr[x]
        }
    }
    arr[0] = temp
    return (arr)
}
console.log(minToFront([4,2,1,3,5]))