// #1
function lastFew(arr) {
    for (x = 0; x < arr.length; x++) {
    }
    arr.splice(0, 2)
    return(arr)
}
console.log(lastFew([2,4,6,8,10],3))

// #2 NOT SURE WHATS ASKING
function mathHelp(M, B, X) {


    return(X)
}
console.log(mathHelp(10, 15));

// #3 NOT SURE WHATS ASKING
function whatHappensToday() {
    volcanoes = (100 / 10) * .1//1
    tsunamis = (100 / 15) * .1//.15
    earthquakes = (100 / 20) * .1//.2
    blizzards = (100 / 25) * .1//.25
    meteors = (100 / 30) * .1//.3
    console.log("There is a \n" +
                `${volcanoes}% that a volcanoe will erupt today\n` +
                `${tsunamis}% that a tsunami will hit today\n` +
                `${earthquakes}% that an earthquake will occur today\n` +
                `${blizzards}% that a blizzard will blizz today\n` +
                `${meteors}% that a meteor will land today`)
}
console.log(whatHappensToday());

// #4 NOT SURE WHATS ASKING
function whatHappensToday() {
    volcanoes = (100 / 10) * .1//1
    tsunamis = (100 / 15) * .1//.15
    earthquakes = (100 / 20) * .1//.2
    blizzards = (100 / 25) * .1//.25
    meteors = (100 / 30) * .1//.3
    console.log("There is a \n" +
                `${volcanoes}% that a volcanoe will erupt today\n` +
                `${tsunamis}% that a tsunami will hit today\n` +
                `${earthquakes}% that an earthquake will occur today\n` +
                `${blizzards}% that a blizzard will blizz today\n` +
                `${meteors}% that a meteor will land today`)
}
console.log(whatHappensToday());

// #5 DOES NOT SHOW DECIMAL PLACES
function soaringIQ(arr) {
    modest = 101
    modest.toFixed(2)
    days = 98
    for (x = 0; x < days; x++) {
        increment = .01 * x
        arr.push(modest) + increment
    }
    return(arr.length - 1)
}
console.log(soaringIQ([]));

// #6
function letterGrade(score) {
    if (score >= 90) {
        console.log(`Score:${score}. Grade: A`)
    } else if ((score >= 80) && (score <= 89)) {
        console.log(`Score:${score}. Grade: B`)
    } else if ((score >= 70) && (score <= 79)) {
        console.log(`Score:${score}. Grade: C`)
    } else if((score >= 60) && (score <= 69)) {
        console.log(`Score:${score}. Grade: D`)
    } else if (score < 60) {
        console.log(`Score:${score}. Grade: F`)
    }
}
console.log(letterGrade(92));

// #7 OPTIONAL
function letterGrade(score) {
    switch(score == score) {
        case 'A':
            if (score >= 98){
                console.log(`Score:${score}. Grade: A+`)
                }
            if ((score <= 93) && (score >= 90)) {
                    console.log(`Score:${score}. Grade: A-`)
                }
            if ((score >= 94) && (score <= 97)) {
                console.log(`Score:${score}. Grade: A`)
            }
            break;
        case 'B':
            if (score >= 88){
                console.log(`Score:${score}. Grade: B+`)
                }
            if ((score <= 83) && (score >= 80)) {
                    console.log(`Score:${score}. Grade: B-`)
                }
            if ((score >= 84) && (score <= 87)) {
                console.log(`Score:${score}. Grade: B`)
            }
            break;
        case 'C':
            if (score >= 78){
                console.log(`Score:${score}. Grade: C+`)
                }
            if ((score <= 73) && (score >= 70)) {
                    console.log(`Score:${score}. Grade: C-`)
                }
            if ((score >= 74) && (score <= 77)) {
                console.log(`Score:${score}. Grade: C`)
            }
            break;
        case 'D':
            if (score >= 68){
                console.log(`Score:${score}. Grade: D+`)
                }
            if ((score <= 63) && (score >= 60)) {
                    console.log(`Score:${score}. Grade: D-`)
                }
            if ((score >= 64) && (score <= 67)) {
                console.log(`Score:${score}. Grade: D`)
            }
            break;
        case 'F':
            if (score <= 60){
                console.log(`Score:${score}. Grade: F`)
                }
            break;
    }
    // if (score >= 90) {
    //     console.log(`Score:${score}. Grade: A`)
    //     if (score >= 98){
    //     console.log(`Score:${score}. Grade: A+`)
    //     } else if (score <= 93){
    //         console.log(`Score:${score}. Grade: A-`)
    //     }
    // } else if ((score >= 80) && (score <= 89)) {
    //     console.log(`Score:${score}. Grade: B`)
    // } else if ((score >= 70) && (score <= 79)) {
    //     console.log(`Score:${score}. Grade: C`)
    // } else if((score >= 60) && (score <= 69)) {
    //     console.log(`Score:${score}. Grade: D`)
    // } else if (score < 60) {
    //     console.log(`Score:${score}. Grade: F`)
    // }
}
console.log(letterGrade(92));