def sum_pairs(number_list, goal):
    ret = []
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if (number_list[i] + number_list[j]) == goal:
                ret.append([number_list[i], number_list[j]])
    return ret