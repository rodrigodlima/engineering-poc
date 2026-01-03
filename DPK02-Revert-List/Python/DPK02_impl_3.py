def revert_list(list):
    list_reverse = []
    len_list = len(list)
    i = 1
    while i <= len_list:
        list_reverse.append(list[len_list -i])
        i = i+1
    return list_reverse


values = [1, 2, 3, 4, 5]
print(revert_list(values)) 