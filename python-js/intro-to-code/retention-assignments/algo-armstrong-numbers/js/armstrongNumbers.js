// How can you make this more scalable and reusable later?

function getDigits(number) {
    let ret = [0, 0, 0];
    if (number >= 100) {
        let val = Math.floor(number / 100);
        ret[2] = val;
        number -= val * 100;
    }
    if (number >= 10) {
        let val = Math.floor(number / 10);
        ret[1] = val;
        number -= val * 10;
    }
    if (number >= 1) {
        let val = Math.floor(number / 1);
        ret[0] = val;
    }
    return ret;
}

exports.findArmstrongNumbers = function(numbersList) {
    let ret = [];
    const singleDigitVals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    const doubleDigitVals = singleDigitVals.map(function(element) { return Math.pow(element, 2) });
    const tripleDigitVals = singleDigitVals.map(function(element) { return Math.pow(element, 3) });
    
    for (let i = 0; i < numbersList.length; i++) {
        let digitsList = getDigits(numbersList[i]);
        let sum = 0;
        // Calculate the sum based on armstrong number equation
        if (digitsList[2] > 0) {
            sum = tripleDigitVals[digitsList[2]] + tripleDigitVals[digitsList[1]] + tripleDigitVals[digitsList[0]];
        }
        else if (digitsList[1] > 0) {
            sum = doubleDigitVals[digitsList[2]] + doubleDigitVals[digitsList[1]] + doubleDigitVals[digitsList[0]];
        }
        else {
            sum = singleDigitVals[digitsList[2]] + singleDigitVals[digitsList[1]] + singleDigitVals[digitsList[0]];
        }
        // Check if the number is an armstrong number
        if (sum == numbersList[i]) {
            ret.push(sum);
        }
    }
    return ret;
};
