def create_value_index_list_sorted(arr):
    ret = []
    for i in range(len(arr)):
        ret.append((arr[i], i))
    ret = sorted(ret, key=lambda elem: elem[0])
    return ret    

def create_value_index_list_reversed(arr):
    ret = []
    for i in range(len(arr)):
        ret.append((arr[i], i))
    ret = sorted(ret, key=lambda elem: elem[0], reverse=True)
    return ret

def linear_search_unsorted(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return [i, steps]

def binary_search_unsorted(arr, target):
    steps, prev_idx = 0, -1
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
        if idx == prev_idx:
            break
        prev_idx = idx

# Linear Search
def linear_search_sorted_words(word_list, target_word):
    steps = 0
    for i in range(len(word_list)):
        steps += 1
        if word_list[i] == target_word:
            return [i, steps]

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    # Your code here
    steps, offset = 0, 0
    while True:
        steps += 1
        mid = int(len(word_list)/2)
        curr = word_list[mid]
        if curr > target_word:
            word_list = word_list[:mid]
        elif curr < target_word:
            # I think mid + 1 for the offset, correction because indexing starts at 0
            offset += mid + 1
            word_list = word_list[mid+1:]
        else:
            return [mid + offset, steps]

# Linear Search
def linear_search_last_occurrence(arr, target):
    steps = 0
    for i in reversed(range(len(arr))):
        steps += 1
        if arr[i] == target:
            return [i, steps]

# Binary Search
def binary_search_last_occurrence(arr, target):
    sorted_arr = create_value_index_list_reversed(arr)
    steps, prev_idx = 0, -1
    while True:
        steps += 1
        mid = int(len(sorted_arr)/2)
        elem, idx = sorted_arr[mid]
        if elem > target:
            sorted_arr = sorted_arr[mid:]
        elif elem < target:
            sorted_arr = sorted_arr[:mid+1]
        else:
            while elem == target:
                steps += 1
                mid += 1
                prev_idx = idx
                elem, idx = sorted_arr[mid]
            return [prev_idx, steps]
        if prev_idx == idx:
            break
        prev_idx = idx

'''
# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
# sorting sacrifices efficiency gains of binary search since sorting runs in O(n)
# meaning for an unsorted list, linear search makes more sense than binary search
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(unsorted_list, target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
# no sorting needed, so binary search is more efficient
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
# sorting needed, so linear search is simpler and just as efficient as binary search
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(occurrence_list, target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")
'''