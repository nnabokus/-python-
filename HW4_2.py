def even_index_sum(lst):
    if not lst:
        return 0
    total = sum(lst[::2])
    return total * lst[-1]


examples = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for lst in examples:
    print(lst, "=>", even_index_sum(lst))
