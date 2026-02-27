sumPairs = function(numberList, goal) {
    let ret = [];
    for (let i = 0; i < numberList.length; i++) {
        for (let j = i+1; j < numberList.length; j++) {
            if (numberList[i] + numberList[j] == goal) {
                ret.push([numberList[i], numberList[j]]);
            }
        }
    }
    return ret;
};

module.exports = sumPairs;