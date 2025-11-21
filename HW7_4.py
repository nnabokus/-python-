def common_elements():
    list3 = [i for i in range(100) if i % 3 == 0]
    list5 = [i for i in range(100) if i % 5 == 0]

    set3 = set(list3)
    set5 = set(list5)

    return set3 & set5

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("OK")
