def revert_list(list):
    len_string = len(list)
    for len_string in list:
        list_reverse = list_reverse + list[len_string - 1]
        len_string = len_string - 1
    return list_reverse

values = [1, 2, 3, 4, 5]
print(revert_list(values)) 