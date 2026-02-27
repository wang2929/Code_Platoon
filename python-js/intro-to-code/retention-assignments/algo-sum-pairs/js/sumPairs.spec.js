const sumPairs = require("./sumPairs.js");

/*
sum_pairs([1,2,3,4,5], 9) # [[4,5]]
sum_pairs([1,2,3,4,5], 7) # [[2,5], [3,4]]
sum_pairs([3, 1, 5, 8, 2], 27) # 'unable to find pairs'
*/
// Don't forget to add your tests :)
describe("Tests valid sum pair problems with solution", () => {
    test("tests sumPairs([1,2,3,4,5], 9) == [[4,5]]", () => {
        expect(sumPairs([1,2,3,4,5], 9)).toStrictEqual([[4,5]]);
    });
    test("tests sumPairs([1,2,3,4,5], 7) == [[2,5], [3,4]]", () => {
        expect(sumPairs([1,2,3,4,5], 7)).toStrictEqual([[2,5], [3,4]]);
    });
});

describe("Tests valid sum pair problems with no solution", () => {
    test("tests sumPairs([3, 1, 5, 8, 2], 27) == []", () => {
        expect(sumPairs([3, 1, 5, 8, 2], 27)).toStrictEqual([]);
    });
});
