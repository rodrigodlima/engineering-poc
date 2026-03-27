def reversed_list(lst):
    result = list(reversed(lst))
    return result


values = list(range(1, 10000001))
print(reversed_list(values))
