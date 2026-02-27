def linear_search(value_to_find, array_to_search_through):
    # your code here
    for i in range(len(array_to_search_through)):
        if array_to_search_through[i] == value_to_find:
            return i
    return None

def linear_search_global(value_to_find, array_to_search_through):
    # your code here
    ret = []
    for i in range(len(array_to_search_through)):
        if array_to_search_through[i] == value_to_find:
            ret.append(i)
    return ret