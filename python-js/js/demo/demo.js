function regExTest(x) {
    const pinRegEx = /^(?:[0-9]{4}|[0-9]{6})$/;
    return pinRegEx.test(x);
}

function filterTest(x) {
    return x.filter((elem) => elem > 5);
}

console.log(filterTest([1,, 3, 5, 7, 9, 11]));