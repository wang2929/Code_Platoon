function testStuff(x) {
    const pinRegEx = /^(?:[0-9]{4}|[0-9]{6})$/;
    return pinRegEx.test(x);
}

console.log(testStuff("1234")); // expect true
console.log(testStuff("12345")); // expect false
console.log(testStuff("123456")); // expect true
console.log(testStuff("12341234")); // expect false