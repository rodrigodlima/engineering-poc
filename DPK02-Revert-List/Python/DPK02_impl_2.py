def revert_list(list):
    list_reverse = []
    len_list = len(list)
    for i in range(len_list):
        list_reverse.append(list[len_list - 1 - i])
    return list_reverse

values = [1, 2, 3, 4, 5]
print(revert_list(values)) 