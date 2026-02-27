def get_digits(number):
    hundreds, tens, ones = 0, 0, 0
    if number >= 100:
        hundreds = int(number / 100)
        number -= hundreds * 100
    if number >= 10:
        tens = int(number / 10)
        number -= tens * 10
    if number >= 0:
        ones = number
    return hundreds, tens, ones

# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    ret = []
    
    # only need up to 3 digits of armstrong numbers, so only up to power of 3
    digits_power_one = [x for x in range(10)]
    digits_power_two = [x**2 for x in range(10)]
    digits_power_three = [x**3 for x in range(10)]
    
    # Goal is to take every digit of a number and add up
    # single digits - the digit
    # double digits - add the square of the digits
    # triple digits - add the cube of the digits
    for numb in numbers:
        hundreds, tens, ones = get_digits(numb)
        if hundreds != 0:
            calculated_sum = digits_power_three[hundreds] + digits_power_three[tens] + digits_power_three[ones]
        elif tens != 0:
            calculated_sum = digits_power_two[tens] + digits_power_two[ones]
        else:
            calculated_sum = digits_power_one[ones]
        if calculated_sum == numb:
            ret.append(numb)
    return ret