function factorial(num) {
    let answer = 1;

    for(let i = num; i > 1; i--) {
        answer = answer * i;
    }

    return answer;
}

module.exports = factorial;