def create_value_index_list_sorted(arr):
    ret = []
    for i in range(len(arr)):
        ret.append((arr[i], i))
    sorted(ret, key=lambda elem: elem[0])
    return ret    

def create_value_index_list_reversed(arr):
    ret = []
    for i in range(len(arr)):
        ret.append((arr[i], i))
    list(reversed(ret, key=lambda elem: elem[0]))
    return ret

def linear_search_unsorted(arr, target):
    steps = 0
    sorted_arr = create_value_index_list_sorted(arr)
    for elem, idx in sorted_arr:
        steps += 1
        if elem == target:
            return [idx, steps]

def binary_search_unsorted(arr, target):
    steps, prev_mid = 0, -1
    sorted_arr = create_value_index_list_sorted(arr)
    while True:
        steps += 1
        mid = int(len(sorted_arr)/2)
        val, idx = sorted_arr[mid]
        if target > val:
            sorted_arr = sorted_arr[mid+1:]
        elif target < val:
            sorted_arr = sorted_arr[:mid]
        else:
            return [idx, steps]
        if mid == prev_mid:
            break
        prev_mid = mid

# Linear Search
def linear_search_sorted_words(word_list, target_word):
    # Your code here
    return linear_search_unsorted(word_list, target_word)

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    # Your code here
    return binary_search_unsorted(word_list, target_word)

# Linear Search
def linear_search_last_occurrence(arr, target):
    steps = 0
    sorted_arr = create_value_index_list_sorted(arr)
    for elem, idx in sorted_arr:
        steps += 1
        if elem == target:
            return [idx, steps]

# Binary Search
def binary_search_last_occurrence(arr, target):
    arr.reverse()
    steps = 0
    while True:
        steps += 1
        mid = int(len(arr)/2)
        if target > arr[mid]:
            arr = arr[mid:]
        elif target < arr[mid]:
            arr = arr[:mid]
        else:
            while (arr[mid]) == target:
                mid += 1
            return [mid-1, steps]

# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")