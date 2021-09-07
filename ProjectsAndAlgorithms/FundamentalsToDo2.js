// #1
function countDown(a) {
    arr = []
    for ( i = a ; i >= 0; i-- ){
        arr.push(i)
    }
    return arr
}
console.log(countDown(10))

// #2
function pandr(a) {
    arr = []
    arr.push(2, a)
    console.log(arr[0])
    return(console.log(arr[1]))
}
pandr(5);

// #3
function fpl(a) {
    arr = [a,7,12,34,98.12,12]
    return (console.log(arr[0] + arr.length))
}
fpl(1>0);

//4
arr = [1,3,5,7,9,13]
count = 0
function GreaterThan() {
    for (x = 0; x<10; x++)
        if (arr[x] > arr[2]) {
            console.log(arr[x])
            count++
        }
        console.log(count)
}
GreaterThan();

// #5
count = 0
function generalized(a) {
    arr = []
    for ( i = a ; i >= 0; i-- ){
        arr.push(i)
        if (arr[i] > arr[2]) {
            count++
        }
    }
    return arr
}
console.log(generalized(20))
console.log(count)
generalized();

// #6
function lengthvalue(a, b) {
    arr = []
    for ( x = 0; x < a; x++) {
        arr.push(b)
    }
    if ( a == b ) {
        console.log("Jinx!")
    }
    console.log(arr)
    return(arr)
}
lengthvalue(6, 6);

// #7
function firstValue(a) {
    arr = []
    for ( x = 0; x < a; x++) {
        arr.push(x)
        if (arr[0] > arr.length) {
            console.log("Too Big!")
            if (arr[0] < arr.length) {
                console.log ("Too Small!")
            }
        } else {
            if (arr[0] == arr.length) {
                console.log("Just Right")
            }
        }
    }
}
firstValue(10);

// #8

function fahrenheitToCelsius(fDegrees) {
    celsius = (fDegrees - 32) * 5/9
    return (console.log(celsius))
}
fahrenheitToCelsius(125);

// #9 
function celsiusToFahrenheit(cDegrees) {
    fahrenheit = (cDegrees * 9/5) + 32
    return (console.log(fahrenheit))
}
celsiusToFahrenheit(125);