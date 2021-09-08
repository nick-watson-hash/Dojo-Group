// #1
function biggieSize(arr) {
    for (x = 0; x <= arr.length; x++) {
        if (arr[x] > 0 ) {
            arr[x] = "Big"
        }
    }
    console.log(arr)
    return(arr)
}
biggieSize([-12,23,-43,1, 0, -1000, 52]);

// #2
function printLow (arr) {
    min = arr[0]
    max = arr[0]
    for ( var x = 0; x < arr.length; x++) {
        console.log(min, max)
        if (arr[x] < min) {
            min = arr[x]
        }
        if (arr[x] > max) {
            max = arr[x]
        }
    }
    console.log(min)
    return(max)
}
console.log(printLow([20,-3,100,21,0,1,-24,-12]))

// #3
function printOne(arr) {
    for ( x = 0; x < arr.length; x++) {
        if (arr[x] % 3 == 0 ) {
            console.log(arr[arr.length - 2])
            return(arr[x])
        }
    }
}
console.log(printOne([20,-3,100,21,0,1,-12]))

// #5
function double(arr) {
    for (x = 0; x < arr.length; x++) {
        arr[x] = arr[x] * 2
    }
    return(arr)
}
console.log(double([1,2,3]));

// #6
function countPositives(arr) {
    counter = 0
    for (x = 0; x < arr.length; x++) {
        if (arr[x] > 0 ) {
            counter++
        }
    }
    arr[arr.length - 1 ] = counter
    return (arr)
}
console.log(countPositives([-1,1,1,1]))

// #7
function evensOdds(arr) {
    evencounter = 0
    oddcounter = 0
    for (x = 0; x < arr.length; x++) {
        if (arr[x] % 2 == 0) {
            evencounter++
        }
        if (arr[x] % 2 == 1) {
            oddcounter++
        }
    }
    if (evencounter = 3) {
        console.log("Even more so!")
    }
    if (oddcounter = 3) {
        console.log("That's odd!")
    }
}
console.log(evensOdds([20,4,100,21,7,13,-12]))

// #8
function increment(arr) {
    sum = 0
    for (x = 0; x < arr.length; x++) {
        if (arr[x] % 2 == 1){
            arr[x]++
            sum = sum + arr[x]
        }
    }
    console.log(sum)
    return (arr)
}
console.log(increment([20,4,100,21,7,13,-12]))

// #9
function previous(arr) {
    for (x = 0; x < arr.length; x++) {
        if (arr[x][0] = String ) {
            arr[x] = arr[x].length
        }
    }
    test = arr.shift()
    arr.push(test)
    return(arr)
}
console.log(previous(['bob','joe','jill','hill','steve','hank','cris']))

// #10
function sevenMost(arr){
    for (x = 0; x < arr.length; x++) {
        arr[x] = arr[x] +7
    }
    arr.shift()
    return(arr)
}
console.log(sevenMost([20,4,100,21,7,13,-12]))

// #11
function reverse(arr) {
    for (x = 0; x < arr.length; x++) {
        arr.splice(x, 0, arr.pop())
    }
    return (arr)
}
console.log(reverse([3,1,6,4,2]))

// #12
function negative(arr) {
    for (x = 0; x < arr.length; x++) {
        if (arr[x] > 0) {
            arr[x] = arr[x] * -1
        }
    }
    return (arr)
}
console.log(negative([1,-3,5]))

// #13
function hungry(arr) {
    //boolean keeps track if food hasn't been found
    hungrystring = true
    for (x = 0; x < arr.length; x++) {
        if (arr[x] == ("food")) {
            console.log("yummy")
            hungrystring = false
        }
    }
    if (hungrystring == true) {
        console.log("I'm hungry")
    }
    return(arr)
}
console.log(hungry(['bob','bob','food','food','steve','hank','cris']))

// #14 HELP
function centerSwap(arr) {
    lastId = arr[arr.length - 1] //6
    firstId = arr[0] //1
    for (x = 0; x < arr.length; x++) {
        lastId = arr[0]
        arr[0] = firstId
    }
    return(arr)
}
console.log(centerSwap([1,2,3,4,5,6]))

// #15
function scale(arr) {
    for (num = 0; num < arr.length; num++) {
        arr[num] = arr[num] * num
    }
    return(arr)
}
console.log(scale([1,2,3,4,5,6]))