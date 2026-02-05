const factorial = require("./factorial.js");

describe("Testing 4 and 5", () => {
    test("Tests factorial(4) is 24", () => {
    // Assertions in javascript
    expect(factorial(4)).toBe(24);
    })

    test("Tests factorial(5) is 120", () => {
        // Assertions in javascript
        expect(factorial(5)).toBe(120);
    })
    })

describe("Testing 0 and 1", () => {
    test("Tests factorial(0) is 1", () => {
    // Assertions in javascript
    expect(factorial(1)).toBe(1);
    })

    test("Tests factorial(1) is 1", () => {
    // Assertions in javascript
    expect(factorial(1)).toBe(1);
    })
})