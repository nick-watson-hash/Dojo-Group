// #1
function sigma(num) {
    sum = 0
    for ( var x = 1; x <= num; x++) {
        sum = sum + x
    }
    return (sum)
}
console.log(sigma(3));

// #2
function factorial(num) {
    sum = 1
    for ( var x = 1; x <= num; x++) {
        sum = sum * x
    }
    return (sum)
}
console.log(factorial(5));

// #3
function drawLeftStars(num) {
    star = "*"
    for ( var x = 0; x <= num; x++) {
    }
    return(star.repeat(num))
}
console.log(drawLeftStars(15));

// #4
function drawRightStars(num) {
    star = "*"
    arr = []
    for ( var x = 0; x <= num; x++) {
        arr.push(star)
    }
    return(arr)
}
console.log(drawRightStars(75));

// #5
function drawCenteredStars(num) {

}
