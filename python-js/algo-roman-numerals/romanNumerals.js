function toRomanLazy(num) {
  let output = "";
  let romanNumeralsToArabic = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 };
  let romanNumeralPriorityOrder = ["M", "D", "C", "L", "X", "V", "I"];
  for (let priority of romanNumeralPriorityOrder) {
    let floor = Math.floor(num / romanNumeralsToArabic[priority]);
    if (floor == 0) {
      continue;
    }
    let result = priority.repeat(floor);
    output = output.concat(result);
    num -= floor * romanNumeralsToArabic[priority];
  }
  return output;
}

function toRoman(num) {
  let output = "";
  let romanNumeralsToArabic = { "I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "C":100, "CD":400, "D":500, "CM":900, "M":1000 };
  let romanNumeralPriorityOrder = ["M", "CM", "D", "CD", "C", "L", "XL", "X", "IX", "V", "IV", "I"];
  for (let priority of romanNumeralPriorityOrder) {
    let floor = Math.floor(num / romanNumeralsToArabic[priority]);
    if (floor == 0) {
      continue;
    }
    let result = priority.repeat(floor);
    output = output.concat(result);
    num -= floor * romanNumeralsToArabic[priority];
  }
  return output;
}

module.exports = { toRoman, toRomanLazy };
