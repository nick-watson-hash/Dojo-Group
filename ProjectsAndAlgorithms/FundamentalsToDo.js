// #1:
var myNumber = 42
var myName = "Nick"
var myNumber = "Nick"
var myName = 42

console.log(myNumber)
console.log(myName)

// #2
for (var num = -52; num <= 1066; num++) {
    console.log(num)
}

// #3
function beCheerful() {

for (var num = 0; num < 99; num++) {
    console.log("Good Morning!")
}

}
beCheerful()

// #4
for (var num = -300; num <= 0; num + 3 ) {
    if ((num = -3) || (num = -6)) {
        continue;
    }
    console.log(num)
}

// #5
num = 2000
while (num <= 5281) {
    num++;
    console.log(num);
}

// #6
var month = 12
var day = 15
function birthday(a, b) {
    if (((a == month) && (b == day)) || (( b == month) && (a == day))) {
        console.log("How did you know")
    } else {
        console.log("Just another day....")
    }
}
birthday(12, 1);

// #7 stuck
function leapYear(a) {
    for (var year = 1; year <= a; year++ ) {
        if (year % 4 == 0 ) {
            if (year % 100 == 0) {
                if (year % 400 == 0) {
                    console.log("This is a leap year")
                    console.log(year)
                } else {
                    console.log("This is not a leap year")
                    console.log(year)
                }
            } else {
                console.log("This is a leap year")
                console.log(year)
            }
        }
    }
}
leapYear(600);

// #8
num = 507
count = 0
while (num <= 4096) {
    if (num > 4096 ){
        break;
    }
    num = num + 5;
    console.log(num)
    count++;
}
console.log(count)

// #9
num = 0
while (num < 60000) {
    num = num + 6
    console.log(num)
}

// #10
for (num = 0; num <= 100; num++) {
    console.log(num)
    if (num % 5 === 0) {
        console.log("Coding")
    }
    if (num % 10 === 0) {
        console.log("Dojo")
    }
}

// #11
function whatDo(incoming) {
    console.log(incoming)
}
whatDo();

// #12 stuck
count = 0
for ( num = -300000; num < 300000; num++) {
    if (num % 3 === 0) {
        num = num + count
    }
}
console.log(count)

// #13
num = 2016
while (num > 0) {
    num = num - 4
    if (num <= 1)  {
        break;
    }
    console.log(num)
}

// #14 DONT UNDERSTAND

// #15 DONT UNDERSTAND