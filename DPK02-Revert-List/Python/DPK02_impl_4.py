def revert_list(lst):
    result = []
    i = len(lst) - 1

    while True:
        if i < 0:
            break
        result.append(lst[i])
        i -= 1

    return result


#values = [1, 2, 3, 4, 5]
values = list(range(1, 10000001))
print(revert_list(values))
