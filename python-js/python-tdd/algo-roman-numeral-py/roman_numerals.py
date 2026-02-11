def to_roman(num):
    # write your code here!
    output = ""
    roman_to_arabic = { "I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
    priority = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    for idx in range(len(priority)):
        current_pri = priority[idx]
        if (repeat := int(num/roman_to_arabic[current_pri])) == 0:
            continue
        output += current_pri*repeat
        num = num - repeat*roman_to_arabic[current_pri]
    return output