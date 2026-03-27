def revert_list(list):
    list_reverse = []
    len_list = len(list)
    i = 1
    while i <= len_list:
        list_reverse.append(list[len_list - i])
        i = i+1
    return list_reverse


values = list(range(1, 10000001))
print(revert_list(values))
