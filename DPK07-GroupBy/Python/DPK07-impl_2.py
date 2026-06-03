def group_by(items, size):
    result = []
    group = []
    count = 0

    for item in items:
        group = group + [item]
        count = count + 1
        if count == size:
            result = result + [group]
            group = []
            count = 0

    if count > 0:
        result = result + [group]

    return result


# Tests
print(group_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(group_by(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))
