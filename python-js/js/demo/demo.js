function regExTest(x) {
    const pinRegEx = /^(?:[0-9]{4}|[0-9]{6})$/;
    return pinRegEx.test(x);
}

function filterTest(x) {
    return x.filter((elem) => elem > 5);
}

function vowels() {
    return ['A','E','I','O','U','Y','a','e','i','o','u','y']
}

`space is here`.split('').map((char) => console.log(char));
console.log(vowels().indexOf(' '))