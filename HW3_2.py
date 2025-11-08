# Приклад 1
lst = [12, 3, 4, 10]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)

# Приклад 2
lst = [1]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)

# Приклад 3
lst = []
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)

# Приклад 4
lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
