var testArr = [6,3,5,1,2,4]

let sum = 0;

for(let num = 0; num < testArr.length; num++) {
    sum = sum + testArr [num]
    console.log("Num:"+ testArr[num] + ", Sum:"+sum)
    testArr[num] = testArr[num] * num
}
console.log(testArr)
