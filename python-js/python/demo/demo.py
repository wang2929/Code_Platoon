def make_array():
    return [0, 1, 2, 3]

def do_thing(x, y):
    msg = "I'm taking up space"
    return x + y

def product(arr_input):
    ret = 0
    for number in arr_input:
        ret = do_thing(ret, number)
    return ret

print(product(make_array()))