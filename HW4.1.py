def move_zeros(lst):
    zero_count = lst.count(0)
    non_zero = [x for x in lst if x != 0]
    return non_zero + [0] * zero_count


examples = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for lst in examples:
    print(lst, "->", move_zeros(lst))
