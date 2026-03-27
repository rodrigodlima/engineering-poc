def revert_list(list):
    list_reverse = []
    len_list = len(list)
    for i in range(len_list):
        list_reverse.append(list[len_list - 1 - i])
    return list_reverse


values = list(range(1, 10000001))
print(revert_list(values))
