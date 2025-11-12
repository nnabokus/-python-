examples = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for lst in examples:
    if not lst:
        result = 0
    else:
        total = sum(lst[::2])
        result = total * lst[-1]
    print(lst, "=>", result)
