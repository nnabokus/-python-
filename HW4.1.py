examples = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for lst in examples:
    zero_count = lst.count(0)
    non_zero = [x for x in lst if x != 0]
    result = non_zero + [0] * zero_count
    print(lst, "->", result)
