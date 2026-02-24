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

const x = ['h','e','l','l',' ','o']
console.log(`removed ${x.splice(1, 1)}, now have ${x}`);
const word = "WhAtS uP yO"
const titleCase = word.toLowerCase().split(' ').reduce((ret, word) => ret + word.charAt(0).toUpperCase() + word.slice(1) + " ", "")

// for (let i = 0; i < 10; i++) {
//     console.log(Math.floor(Math.random() * 5))
// }
