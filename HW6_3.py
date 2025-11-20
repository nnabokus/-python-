n = input("Введіть будь-ласка число:")
while int(n) > 9:
    result = 1
    for digit in n:
        result *=int(digit)
    n = str(result)
print(n)
